#!/usr/bin/env bash
# create_and_push.sh
# Usage: ./create_and_push.sh <github-username> <repo-name>
# Example: ./create_and_push.sh yourusername wifi-sniffer

set -e
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <github-username> <repo-name>"
  exit 1
fi

GH_USER="$1"
REPO="$2"

git init
git add .
git commit -m "Initial commit: offline pcap analyzer (educational)"
git branch -M main

# Check GH CLI auth
if ! gh auth status >/dev/null 2>&1; then
  echo "Please run: gh auth login"
  exit 1
fi

# Create repo under specified username (must be your account or organization you control)
gh repo create "$GH_USER/$REPO" --public --description "offline pcap analyzer (educational) - python" --confirm

git push -u origin main
echo "Repository created and pushed: https://github.com/$GH_USER/$REPO"
