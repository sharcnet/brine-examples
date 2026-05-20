# Python example

Runs two OpenAI-compatible API calls against SHARCNET Brine:

1. `GET /models` to list available models.
2. `POST /chat/completions` to ask `gemma-4-31B-it` a question.

This example uses only the Python standard library.

```bash
cp ../.env.example ../.env
$EDITOR ../.env
python3 list_models_and_ask_gemma.py
```
