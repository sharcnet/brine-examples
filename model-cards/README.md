# SHARCNET Brine model cards

Public details for models currently available through the SHARCNET Brine OpenAI-compatible API.

The live model list from `GET /v1/models` is authoritative for availability. Models may be added, changed, or retired during the pilot.

| Model | Context limit | Tool calling | Precision notes |
| --- | ---: | --- | --- |
| `gemma-4-31B-it` | 32,768 tokens | Supported | No service-level weight quantization configured |
| `gpt-oss-120b` | 131,072 tokens | Supported | FP8 KV cache |
| `Qwen3.6-35B-A3B` | 131,072 tokens | Supported | No service-level weight quantization configured |
| `DeepSeek-V4-Flash-0731` | 131,072 tokens | Supported | FP8 KV cache |

## Service notes

- API keys issued to participants are for inference routes. Administrative LiteLLM routes such as `/model/info` are intentionally unavailable.
- A model's context limit includes both input and generated tokens.
- Tool-calling behaviour varies by model; applications should validate model output rather than assuming every requested tool call will succeed.
- Do not submit Sensitive Data during the pilot.
