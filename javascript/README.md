# JavaScript example

Runs two OpenAI-compatible API calls against SHARCNET Brine:

1. `GET /models` to list available models.
2. `POST /chat/completions` to ask `gemma-4-31B-it` a question.

Requires Node.js 18+ for built-in `fetch`.

```bash
cp ../.env.example ../.env
$EDITOR ../.env
node list-models-and-ask-gemma.mjs
```
