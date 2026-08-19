# /// script
# dependencies = ["requests"]
# ///
"""Record from the microphone and transcribe it with Brine."""

import os
import shutil
import signal
import subprocess
import tempfile

import requests

BASE_URL = os.getenv("BRINE_BASE_URL", "https://brine.example.org/v1")
API_KEY = os.getenv("BRINE_API_KEY", "your-access-key")
MODEL = os.getenv("BRINE_TRANSCRIPTION_MODEL", "whisper-large-v3-turbo")

if not shutil.which("pw-record"):
    raise SystemExit("pw-record is required (install PipeWire tools)")

with tempfile.NamedTemporaryFile(suffix=".wav") as audio:
    input("Press Enter to start recording...")
    recorder = subprocess.Popen(
        ["pw-record", "--rate", "16000", "--channels", "1", audio.name]
    )
    input("Recording. Press Enter to stop...")
    recorder.send_signal(signal.SIGINT)
    recorder.wait()

    response = requests.post(
        f"{BASE_URL}/audio/transcriptions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        data={"model": MODEL},
        files={"file": ("recording.wav", audio, "audio/wav")},
    )
    response.raise_for_status()
    print(response.json()["text"].strip())
