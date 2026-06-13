#!/usr/bin/env bash
# DI Loop Library ダッシュボード起動スクリプト
cd "$(dirname "$0")"
PORT="${1:-8000}"
echo "Starting dashboard at http://localhost:${PORT}"
( sleep 1; command -v open >/dev/null && open "http://localhost:${PORT}" || command -v xdg-open >/dev/null && xdg-open "http://localhost:${PORT}" ) >/dev/null 2>&1 &
python3 -m http.server "$PORT"
