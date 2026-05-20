#!/usr/bin/env node
// List SHARCNET Brine models, then ask the Gemma model a question.
// Requires Node.js 18+ for built-in fetch.

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const repoDir = path.resolve(path.dirname(__filename), "..");

function loadDotenv(filePath) {
  if (!fs.existsSync(filePath)) return;

  for (const rawLine of fs.readFileSync(filePath, "utf8").split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#") || !line.includes("=")) continue;

    const [key, ...rest] = line.split("=");
    const value = rest.join("=").trim().replace(/^['"]|['"]$/g, "");
    if (!process.env[key.trim()]) process.env[key.trim()] = value;
  }
}

async function apiRequest(method, endpoint, payload) {
  const baseUrl = process.env.BRINE_BASE_URL.replace(/\/$/, "");
  const response = await fetch(`${baseUrl}${endpoint}`, {
    method,
    headers: {
      Authorization: `Bearer ${process.env.BRINE_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: payload ? JSON.stringify(payload) : undefined,
  });

  const text = await response.text();
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${text}`);
  }
  return JSON.parse(text);
}

loadDotenv(path.join(repoDir, ".env"));

const missing = ["BRINE_BASE_URL", "BRINE_API_KEY"].filter((name) => !process.env[name]);
if (missing.length > 0) {
  console.error(`Missing required environment variable(s): ${missing.join(", ")}`);
  console.error("Copy .env.example to .env or export the variables in your shell.");
  process.exit(2);
}

const model = process.env.BRINE_MODEL || "gemma-4-31B-it";

console.log("== Listing models ==");
const models = await apiRequest("GET", "/models");
console.log(JSON.stringify(models, null, 2));

console.log(`\n== Asking ${model} ==`);
const completion = await apiRequest("POST", "/chat/completions", {
  model,
  messages: [
    {
      role: "user",
      content: "In two sentences, explain what SHARCNET Brine is useful for.",
    },
  ],
  temperature: 0.2,
  max_tokens: 200,
});

console.log(completion.choices[0].message.content);
