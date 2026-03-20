#!/usr/bin/env bash
set -e

echo "=== CLI tests ==="
cd cli && uv run pytest "$@"
