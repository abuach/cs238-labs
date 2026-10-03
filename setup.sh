#!/usr/bin/env bash
# One-time setup for the CS238 labs (Linux). From your cs238 folder, run:
#     bash cs238-labs/setup.sh
# It's safe to run again.
set -euo pipefail

SERVER="http://ollama2.cs.wallawalla.edu:11434"
LABS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COURSE_DIR="$(dirname "$LABS_DIR")"

if [ ! -f "$COURSE_DIR/pyproject.toml" ]; then
    echo "Couldn't find $COURSE_DIR/pyproject.toml."
    echo "Run 'uv init --python 3.13 --vcs none' in your cs238 folder first (Getting Started, step 3)."
    exit 1
fi

# 1. Install every Python package the labs use, including genai
echo "Installing the lab packages (this can take a few minutes the first time)..."
cd "$COURSE_DIR"
uv add -r "$LABS_DIR/requirements.txt"

# 2. Point genai (and ollama) at the class server, once
LINE="export OLLAMA_HOST=$SERVER"
if grep -qxF "$LINE" ~/.bashrc 2>/dev/null; then
    echo "~/.bashrc already points at the class server."
else
    echo "$LINE" >> ~/.bashrc
    echo "Added OLLAMA_HOST to ~/.bashrc."
fi

# 3. Check which server genai will use (slow the first time, so it's off by default)
# OLLAMA_HOST="$SERVER" uv run python -c "from genai import get_host; print(get_host())"

echo
echo "Done. Now run:  source ~/.bashrc"
echo "(or open a new terminal) so this terminal picks up the server setting."
