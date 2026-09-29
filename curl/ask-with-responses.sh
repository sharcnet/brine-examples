#!/usr/bin/env bash
set -e

# Set BRINE_API_KEY before running this script.
BRINE_BASE_URL="${BRINE_BASE_URL:-https://brine.sharcnet.ca/v1}"
BRINE_API_KEY="${BRINE_API_KEY:?Set BRINE_API_KEY to your Brine access key}"
BRINE_MODEL="${BRINE_MODEL:-DeepSeek-V4-Flash-0731}"

curl "${BRINE_BASE_URL%/}/responses" \
  -H "Authorization: Bearer ${BRINE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"${BRINE_MODEL}\",
    \"input\": \"In two sentences, explain what high performance computing is.\",
    \"max_output_tokens\": 200
  }"
echo
