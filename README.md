# SHARCNET Brine examples

Small demo scripts for the SHARCNET Brine OpenAI-compatible API.

Each script does two things:

1. Lists available models with `GET /models`.
2. Asks the Gemma model: "In two sentences, explain what high performance computing is."

## Set your access details

Either edit the variables near the top of each script, or export them in your shell:

```bash
export BRINE_BASE_URL="https://brine.example.org/v1"
export BRINE_API_KEY="paste-your-access-key-here"
export BRINE_MODEL="gemma-4-31B-it"
```

`BRINE_MODEL` is optional. The default is `gemma-4-31B-it`.

## Run the examples

### curl

```bash
cd curl
./list-models-and-ask-gemma.sh
```

### Python

```bash
cd python
uv run --with requests list_models_and_ask_gemma.py

# Interactive microphone transcription
uv run transcribe_microphone.py
```

### JavaScript

Requires Node.js 18+.

```bash
cd javascript
node list-models-and-ask-gemma.mjs
```

## Model cards

See [`model-cards/README.md`](model-cards/README.md) for public details about currently served models, including context limits and tool support.

## Notes

- Treat `BRINE_API_KEY` as a secret.
- Do not submit Sensitive Data to SHARCNET Brine during the pilot.
