#!/usr/bin/env python3
"""巡检 README/ARTICLES 里的外链，报死链与改名仓库。

用法：
    python scripts/check_links.py [--all]

设计要点（与仓库其他检查同源：宁可说"不确定"，不假装通过）：

* GitHub 仓库链接走 API（`/repos/{owner}/{repo}`），能区分三种情况：
  200 存活 / 404 死链 / 301 改名（API 会跟随，但 `url` 与请求路径不一致即说明改名）。
  带 token 时速率上限 5000/h（CI 里用 `GITHUB_TOKEN`），匿名只有 60/h。
* 其他站点用 HEAD，405/403 视为"活着但拒绝 HEAD"，不判死。
* 连不上（DNS/超时/代理）算 `unknown`，不算死链 —— 不然一次网络抖动就制造一堆假红，
  检查器会被训练成没人信（这个原则来自 RevolutionLA.github.io 的 check-claims.py）。
* 只有确认的 404 才让退出码为 1。

环境变量：GITHUB_TOKEN / GH_TOKEN（可选，强烈建议）
"""
from __future__ import annotations

import argparse
import json
import os
import re
import socket
import sys
import urllib.error
import urllib.request

FILES = ["README.md", "README_EN.md", "ARTICLES.md"]
GH_API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
UA = {"User-Agent": "awesome-YuE-link-check"}

LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
GH_RE = re.compile(r"^https?://github\.com/([^/]+)/([^/#?]+)")


def collect(paths):
    urls = set()
    for p in paths:
        try:
            text = open(p, encoding="utf-8").read()
        except FileNotFoundError:
            continue
        for m in LINK_RE.finditer(text):
            url = m.group(1).rstrip(".,;")
            urls.add(url)
    return sorted(urls)


def gh_status(owner: str, repo: str):
    """返回 (state, detail)。state ∈ ok / renamed / dead / unknown"""
    headers = dict(UA)
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(f"{GH_API}/repos/{owner}/{repo}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = json.load(r)
            full = data.get("full_name", f"{owner}/{repo}")
            if full.lower() != f"{owner}/{repo}".lower():
                return "renamed", full
            return "ok", ""
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "dead", "404 (仓库不存在或已私有)"
        if e.code in (403, 429):
            return "unknown", f"限流 {e.code}"
        return "unknown", f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001 - 网络问题一律 unknown
        return "unknown", type(e).__name__


def http_status(url: str):
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return "ok", str(r.status)
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 429):
            return "ok", f"{e.code}（拒绝 HEAD，视为存活）"
        if e.code == 404:
            return "dead", "404"
        return "unknown", f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return "unknown", type(e).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="同时检查非 GitHub 外链（默认只查 GitHub）")
    args = ap.parse_args()

    urls = collect(FILES)
    gh_seen = {}
    dead, renamed, unknown = [], [], []

    for url in urls:
        m = GH_RE.match(url)
        if m:
            owner, repo = m.group(1), m.group(2).removesuffix(".git")
            key = f"{owner}/{repo}".lower()
            if key in gh_seen:
                continue
            state, detail = gh_status(owner, repo)
            gh_seen[key] = state
            if state == "dead":
                dead.append((url, detail))
            elif state == "renamed":
                renamed.append((url, detail))
            elif state == "unknown":
                unknown.append((url, detail))
        elif args.all:
            state, detail = http_status(url)
            if state == "dead":
                dead.append((url, detail))

    total = len(gh_seen)
    print(f"检查了 {total} 个 GitHub 仓库链接" + (f" + {len(urls) - total} 个其他外链" if args.all else ""))
    for label, items in (("死链", dead), ("改名（请更新为 detail 里的新路径）", renamed), ("无法判定", unknown)):
        if items:
            print(f"\n== {label} {len(items)} 条 ==")
            for url, detail in items:
                print(f"  {url}  ->  {detail}")

    if not (dead or renamed or unknown):
        print("全部存活 ✅")
    # 只有确认的 404 才判死；改名与网络不确定都只报告，不阻断
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
