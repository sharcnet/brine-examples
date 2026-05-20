# curl example

Runs two OpenAI-compatible API calls against SHARCNET Brine:

1. `GET /models` to list available models.
2. `POST /chat/completions` to ask `gemma-4-31B-it` a question.

```bash
cp ../.env.example ../.env
$EDITOR ../.env
./list-models-and-ask-gemma.sh
```
