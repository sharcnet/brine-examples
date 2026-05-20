# SHARCNET Brine examples

Demo scripts for Pilot Participants using the SHARCNET Brine OpenAI-compatible API.

Each example does the same two things:

1. Lists available models with `GET /models`.
2. Sends a real chat question to the Gemma model, defaulting to `gemma-4-31B-it`.

## Configure access

Copy the example environment file and fill in the service URL and your Access Key:

```bash
cp .env.example .env
$EDITOR .env
```

Required settings:

```bash
BRINE_BASE_URL="https://brine.example.org/v1"
BRINE_API_KEY="paste-your-access-key-here"
```

Optional setting:

```bash
BRINE_MODEL="gemma-4-31B-it"
```

You can also export these variables directly in your shell instead of creating `.env`.

## Run the examples

### curl

```bash
cd curl
./list-models-and-ask-gemma.sh
```

### Python

Uses only the Python standard library.

```bash
cd python
python3 list_models_and_ask_gemma.py
```

### JavaScript

Requires Node.js 18+ for built-in `fetch`.

```bash
cd javascript
node list-models-and-ask-gemma.mjs
```

## Notes

- Treat `BRINE_API_KEY` as a secret. Do not commit `.env`.
- Do not submit Sensitive Data to SHARCNET Brine during the pilot.
- The examples use OpenAI-compatible endpoints, so the same request shape works across curl, Python, and JavaScript.
