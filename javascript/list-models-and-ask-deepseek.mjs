#!/usr/bin/env node
// List models, then ask DeepSeek a question.
// Requires Node.js 18+ for built-in fetch.

// Fill these in, or set them before running the script:
//   export BRINE_BASE_URL="https://brine.example.org/v1"
//   export BRINE_API_KEY="your-access-key"
const BRINE_BASE_URL = process.env.BRINE_BASE_URL || "https://brine.example.org/v1";
const BRINE_API_KEY = process.env.BRINE_API_KEY || "your-access-key";
const BRINE_MODEL = process.env.BRINE_MODEL || "DeepSeek-V4-Flash-0731";

const QUESTION = "In two sentences, explain what high performance computing is.";

const headers = {
  Authorization: `Bearer ${BRINE_API_KEY}`,
  "Content-Type": "application/json",
};

console.log("== 1. List available models ==");
const modelsResponse = await fetch(`${BRINE_BASE_URL}/models`, { headers });
console.log(await modelsResponse.text());

console.log(`\n== 2. Ask ${BRINE_MODEL} a question ==`);
const chatResponse = await fetch(`${BRINE_BASE_URL}/chat/completions`, {
  method: "POST",
  headers,
  body: JSON.stringify({
    model: BRINE_MODEL,
    messages: [
      { role: "user", content: QUESTION },
    ],
    temperature: 0.2,
    max_tokens: 200,
  }),
});

const chat = await chatResponse.json();
console.log(chat.choices[0].message.content);
