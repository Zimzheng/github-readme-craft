#!/usr/bin/env python3
"""Check mechanical README delivery invariants without external dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[^)]*)?\)")
HTML_IMAGE_PATTERN = re.compile(r"<img\s+[^>]*src=[\"']([^\"']+)[\"']", re.I)
HTML_LINK_PATTERN = re.compile(r"<a\s+[^>]*href=[\"']([^\"']+)[\"']", re.I)
SENSITIVE_PATTERN = re.compile(
    r"(?:/Users/|C:\\Users\\|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|"
    r"github_pat_[A-Za-z0-9_]{20,}|BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY)",
    re.I,
)


def is_relative_target(target: str) -> bool:
    return not target.startswith(("#", "http://", "https://", "mailto:", "data:"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Check README links, images, and common privacy leaks.")
    parser.add_argument("readme", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()

    if not args.readme.is_file():
        print(f"ERROR: README not found: {args.readme}")
        return 2

    text = args.readme.read_text(encoding="utf-8")
    root = args.repo_root.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not re.search(r"^#\s+\S+", text, re.M):
        errors.append("README must contain a top-level title.")
    if not re.search(r"```(?:bash|sh|shell)?\n", text):
        warnings.append("No shell command block found; confirm that installation or usage instructions are unnecessary.")
    if SENSITIVE_PATTERN.search(text):
        errors.append("README contains a common local-path or credential pattern.")

    targets = IMAGE_PATTERN.findall(text) + LINK_PATTERN.findall(text)
    targets += HTML_IMAGE_PATTERN.findall(text) + HTML_LINK_PATTERN.findall(text)
    for target in targets:
        if not is_relative_target(target):
            continue
        clean_target = target.split("#", 1)[0].split("?", 1)[0]
        if not clean_target:
            continue
        if not (root / clean_target).exists():
            errors.append(f"Relative target does not exist: {target}")

    if not (IMAGE_PATTERN.search(text) or HTML_IMAGE_PATTERN.search(text)):
        warnings.append("No image found; confirm that a visual demonstration would not help readers.")

    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if errors:
        return 1
    print("OK: README mechanical checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
