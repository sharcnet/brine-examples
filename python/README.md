# Python example

Edit the variables at the top of `list_models_and_ask_gemma.py`, or export them first:

```bash
export BRINE_BASE_URL="https://brine.example.org/v1"
export BRINE_API_KEY="paste-your-access-key-here"
```

## Option 1: uv

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager. It can run this script in a temporary environment with `requests` installed, without you manually creating a virtual environment first.

```bash
uv run --with requests list_models_and_ask_gemma.py
```

## Option 2: virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 list_models_and_ask_gemma.py
```
