#!/usr/bin/env bash
set -e

# Fill these in, or set them before running the script:
#   export BRINE_BASE_URL="https://brine.example.org/v1"
#   export BRINE_API_KEY="your-access-key"
BRINE_BASE_URL="${BRINE_BASE_URL:-https://brine.example.org/v1}"
BRINE_API_KEY="${BRINE_API_KEY:-your-access-key}"
BRINE_MODEL="${BRINE_MODEL:-gemma-4-31B-it}"

QUESTION="In two sentences, explain what high performance computing is."

echo "== 1. List available models =="
curl "${BRINE_BASE_URL}/models" \
  -H "Authorization: Bearer ${BRINE_API_KEY}"

echo
echo
echo "== 2. Ask ${BRINE_MODEL} a question =="
curl "${BRINE_BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${BRINE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${BRINE_MODEL}\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"${QUESTION}\"}
    ],
    \"temperature\": 0.2,
    \"max_tokens\": 200
  }"

echo
