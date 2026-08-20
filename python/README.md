# Python example

Edit the variables at the top of `list_models_and_ask_deepseek.py`, or export them first:

```bash
export BRINE_BASE_URL="https://brine.example.org/v1"
export BRINE_API_KEY="paste-your-access-key-here"
```

## Option 1: uv

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager. It can run this script in a temporary environment with `requests` installed, without you manually creating a virtual environment first.

```bash
uv run --with requests list_models_and_ask_deepseek.py
```

### Transcribe your microphone

The transcription script declares its Python dependency for uv and records
through `pw-record`, supplied by PipeWire tools on Linux. Press Enter once to
start recording and again to stop and submit it.

```bash
uv run transcribe_microphone.py
```

## Option 2: virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 list_models_and_ask_deepseek.py
```
