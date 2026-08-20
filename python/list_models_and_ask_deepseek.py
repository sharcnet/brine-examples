#!/usr/bin/env python3
"""List models, then ask DeepSeek a question."""

import os
import requests

# Fill these in, or set them before running the script:
#   export BRINE_BASE_URL="https://brine.example.org/v1"
#   export BRINE_API_KEY="your-access-key"
BRINE_BASE_URL = os.getenv("BRINE_BASE_URL", "https://brine.example.org/v1")
BRINE_API_KEY = os.getenv("BRINE_API_KEY", "your-access-key")
BRINE_MODEL = os.getenv("BRINE_MODEL", "DeepSeek-V4-Flash-0731")

QUESTION = "In two sentences, explain what high performance computing is."

headers = {
    "Authorization": f"Bearer {BRINE_API_KEY}",
    "Content-Type": "application/json",
}

print("== 1. List available models ==")
models_response = requests.get(f"{BRINE_BASE_URL}/models", headers=headers)
print(models_response.text)

print(f"\n== 2. Ask {BRINE_MODEL} a question ==")
chat_response = requests.post(
    f"{BRINE_BASE_URL}/chat/completions",
    headers=headers,
    json={
        "model": BRINE_MODEL,
        "messages": [
            {"role": "user", "content": QUESTION},
        ],
        "temperature": 0.2,
        "max_tokens": 200,
    },
)

answer = chat_response.json()["choices"][0]["message"]["content"]
print(answer)
