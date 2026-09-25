# /// script
# dependencies = ["requests"]
# ///
"""Generate an image from a text prompt with Brine and save it as a PNG."""

import base64
import os
import sys

import requests

BASE_URL = os.getenv("BRINE_BASE_URL", "https://brine.sharcnet.ca/v1")
API_KEY = os.getenv("BRINE_API_KEY", "your-access-key")
MODEL = os.getenv("BRINE_IMAGE_MODEL", "Qwen-Image-2.1")

prompt = " ".join(sys.argv[1:]) or "A lighthouse on Lake Huron at dusk, watercolour"

print("Generating... this usually takes 15-20 seconds.")
response = requests.post(
    f"{BASE_URL}/images/generations",
    headers={"Authorization": f"Bearer {API_KEY}"},
    # Defaults to 768x768. Add "size": "1024x1024" for larger images (slower).
    json={"model": MODEL, "prompt": prompt},
    timeout=300,
)
response.raise_for_status()

with open("image.png", "wb") as image:
    image.write(base64.b64decode(response.json()["data"][0]["b64_json"]))
print("Saved image.png")
