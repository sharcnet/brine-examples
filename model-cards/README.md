# SHARCNET Brine model cards

Public details for models currently available through the SHARCNET Brine OpenAI-compatible API.

The live model list from `GET /v1/models` is authoritative for availability. Models may be added, changed, or retired during the pilot.

| Model | Modality | Service limit | Tool calling | Notes |
| --- | --- | ---: | --- | --- |
| `North-Mini-Code-1.0` | Chat | 256,000 input tokens; 64,000 output tokens | Supported | 30B-total/3B-active MoE; FP8 weights |
| `Qwen3.8-27B` | Chat | 131,072 tokens | Supported | BF16 weights; no service-level weight quantization configured |
| `DeepSeek-V4-Flash-0731` | Chat | 131,072 tokens | Supported | FP8 KV cache |
| `qwen3-embed` | Embedding | 8,192 tokens | Not applicable | 4,096-dimensional vectors |
| `whisper-large-v3-turbo` | Audio transcription | 25 MB upload | Not applicable | Transcription only; this Turbo checkpoint does not support translation |

## Service notes

- API keys issued to participants are for inference routes. Administrative LiteLLM routes such as `/model/info` are intentionally unavailable.
- A chat model's context limit includes both input and generated tokens.
- Embeddings use `POST /v1/embeddings`; transcription uses `POST /v1/audio/transcriptions`.
- The transcription endpoint accepts FLAC, MP3, MP4, MPEG, MPGA, M4A, OGG, WAV, and WEBM audio.
- Tool-calling behaviour varies by model; applications should validate model output rather than assuming every requested tool call will succeed.
- Do not submit Sensitive Data during the pilot.
