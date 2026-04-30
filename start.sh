#!/bin/bash
# NexYouth Flask launcher with SMTP env vars loaded from .env
#
# Usage: ./start.sh
#
# Loads SMTP credentials from .env (gitignored) so EcoClassroom
# completion emails are actually delivered.

set -euo pipefail
cd "$(dirname "$0")"

# Free port 8000 if something is already there
if lsof -i :8000 -t >/dev/null 2>&1; then
  echo "→ Killing existing process on :8000..."
  lsof -i :8000 -t | xargs kill -9 2>/dev/null || true
  sleep 1
fi

# Load .env if present (export each non-comment line)
if [[ -f .env ]]; then
  echo "→ Loading SMTP config from .env"
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
else
  echo "⚠ No .env found — emails will only be logged, not delivered."
fi

PYTHON="${PYTHON:-/Library/Frameworks/Python.framework/Versions/3.11/Resources/Python.app/Contents/MacOS/Python}"
[[ -x "$PYTHON" ]] || PYTHON="python3"

echo "→ Starting Flask on http://localhost:8000"
echo "  SMTP: ${SMTP_HOST:-(none)}:${SMTP_PORT:-} as ${SMTP_USER:-(none)}"
exec "$PYTHON" app.py
