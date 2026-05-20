#!/usr/bin/env bash
set -euo pipefail

# Demo 1: list available models.
# Demo 2: ask the Gemma model a simple question.
#
# Configure either by exporting variables or by creating ../.env from ../.env.example.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

if [[ -f "$REPO_DIR/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$REPO_DIR/.env"
  set +a
fi

: "${BRINE_BASE_URL:?Set BRINE_BASE_URL, for example https://brine.example.org/v1}"
: "${BRINE_API_KEY:?Set BRINE_API_KEY to your SHARCNET Brine access key}"
BRINE_MODEL="${BRINE_MODEL:-gemma-4-31B-it}"

BASE_URL="${BRINE_BASE_URL%/}"

echo "== Listing models =="
curl --fail-with-body --silent --show-error \
  -H "Authorization: Bearer ${BRINE_API_KEY}" \
  "${BASE_URL}/models"

echo
echo
echo "== Asking ${BRINE_MODEL} =="
curl --fail-with-body --silent --show-error \
  -H "Authorization: Bearer ${BRINE_API_KEY}" \
  -H "Content-Type: application/json" \
  -X POST "${BASE_URL}/chat/completions" \
  -d @- <<JSON
{
  "model": "${BRINE_MODEL}",
  "messages": [
    {
      "role": "user",
      "content": "In two sentences, explain what SHARCNET Brine is useful for."
    }
  ],
  "temperature": 0.2,
  "max_tokens": 200
}
JSON

echo
