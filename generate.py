"""
flux-lora-headshots — generate.py
Generate professional AI headshots (or fun portraits) from your trained Flux LoRA.

QUICK START:
  1. Copy .env.example to .env and fill in your keys.
  2. Set TRIGGER_WORD to your LoRA trigger word.
  3. Set MODE to "headshot" or "fun".
  4. Set PROMPT_KEY to choose which prompt to use (see prompts.py).
  5. Run: python generate.py
"""

import os
import re
import random
from pathlib import Path

import requests
import replicate as replicate_lib
from dotenv import load_dotenv

from prompts import HEADSHOT_PROMPTS, FUN_PROMPTS, DEFAULT_HEADSHOT, DEFAULT_FUN

# ---------------------------------------------------------------------------
# CONFIGURATION — edit these before running
# ---------------------------------------------------------------------------

# Your LoRA trigger word (the name you used when training, e.g. "JOHN")
TRIGGER_WORD = "YOUR_NAME"

# Generation mode: "headshot" for professional portraits, "fun" for meme/creative
MODE = "headshot"  # "headshot" | "fun"

# Which prompt to use from prompts.py.
# Headshot options : "corporate" | "corporate_serious" | "corporate_young" | "casual"
# Fun options      : "npc" | "touch_grass" | "main_character" | "rizz" | "side_eye"
#                    "unhinged" | "delulu" | "no_thoughts" | "plot_twist" | "slay"
#                    "medieval_knight" | "superhero" | "astronaut" | "80s"
# Set to None to use the default for the selected mode.
PROMPT_KEY = None

# Inference preset — controls guidance_scale / lora_scale / prompt_strength.
# "identity"   → guidance 1.5, prompt_strength 0.8, lora 0.9  (most recognizable face)
# "balanced"   → guidance 1.75, prompt_strength 0.9, lora 1.1  (best overall ✓)
# "consistent" → guidance 2.0, prompt_strength 0.85, lora 1.0  (stable framing)
# "2025"       → guidance 3.0, prompt_strength 0.8, lora 1.0   (previous best)
PRESET = "balanced"

# Fix a seed for reproducible framing (None = random each run).
# Known good seeds for corporate headshots: 65658157, 3544650143, 846646423
FIXED_SEED = None

# How many images to generate per run (1–4 recommended).
NUM_OUTPUTS = 4

# ---------------------------------------------------------------------------
# INFERENCE PRESETS
# ---------------------------------------------------------------------------

PRESETS = {
    "identity":   {"guidance_scale": 1.5,  "prompt_strength": 0.8,  "lora_scale": 0.9},
    "balanced":   {"guidance_scale": 1.75, "prompt_strength": 0.9,  "lora_scale": 1.1},
    "consistent": {"guidance_scale": 2.0,  "prompt_strength": 0.85, "lora_scale": 1.0},
    "2025":       {"guidance_scale": 3.0,  "prompt_strength": 0.8,  "lora_scale": 1.0},
}

# ---------------------------------------------------------------------------
# CORE FUNCTIONS
# ---------------------------------------------------------------------------

def _sanitize(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '', name).replace(' ', '_')


def _short_label(prompt: str, n: int = 3) -> str:
    skip = {'a', 'the', 'with', 'and', 'in', 'on', 'at', 'to', 'of', 'wearing', 'looking'}
    words, collected = prompt.split(), []
    for w in words:
        cleaned = w.strip(',.').strip()
        if cleaned.lower() not in skip and cleaned and len(cleaned) <= 20:
            collected.append(cleaned)
        if len(collected) >= n:
            break
    return '_'.join(collected)


def download_image(url: str, folder: Path, index: int) -> None:
    response = requests.get(url)
    if response.status_code != 200:
        print(f"  Failed to download image {index} (HTTP {response.status_code})")
        return

    content_type = response.headers.get('content-type', '')
    ext = '.png' if 'png' in content_type else '.jpg'

    existing = [f for f in os.listdir(folder) if f.startswith('image_')]
    numbers = []
    for f in existing:
        try:
            numbers.append(int(f.split('_')[1].split('.')[0]))
        except (IndexError, ValueError):
            continue
    next_num = max(numbers, default=0) + 1

    dest = folder / f'image_{next_num}{ext}'
    with open(dest, 'wb') as fh:
        fh.write(response.content)
    print(f"  Saved: {dest}")


def generate(
    prompt: str,
    seed: int | None = None,
    guidance_scale: float = 2.0,
    lora_scale: float = 1.1,
    prompt_strength: float = 0.8,
    num_outputs: int = 4,
    *,
    num_inference_steps: int = 50,
    output_format: str = "png",
    output_quality: int = 100,
    go_fast: bool = False,
) -> tuple[int, list]:
    """
    Run the Replicate model and return (seed_used, image_urls).

    Max quality defaults: png, go_fast=False, 50 steps, quality=100.
    Lower quality for quick tests: jpg, go_fast=True, 25 steps, quality=80.
    """
    if seed is None:
        seed = random.randint(0, 2**32 - 1)

    client = replicate_lib.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
    output = client.run(
        os.environ["MODEL_NAME"],
        input={
            "prompt": prompt,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "model": "dev",
            "num_outputs": num_outputs,
            "go_fast": go_fast,
            "lora_scale": lora_scale,
            "output_format": output_format,
            "output_quality": output_quality,
            "prompt_strength": prompt_strength,
            "seed": seed,
        },
    )
    return seed, output


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    load_dotenv()

    if TRIGGER_WORD == "YOUR_NAME":
        raise ValueError(
            "Set TRIGGER_WORD to your LoRA trigger word before running (e.g. 'JOHN')."
        )
    for var in ("REPLICATE_API_TOKEN", "MODEL_NAME"):
        if not os.getenv(var):
            raise EnvironmentError(f"Missing required env var: {var}. See .env.example.")

    # Select prompt
    if MODE == "headshot":
        key = PROMPT_KEY or DEFAULT_HEADSHOT
        prompt_fn = HEADSHOT_PROMPTS.get(key)
        if prompt_fn is None:
            raise ValueError(f"Unknown headshot prompt key: '{key}'. Check prompts.py.")
    elif MODE == "fun":
        key = PROMPT_KEY or DEFAULT_FUN
        prompt_fn = FUN_PROMPTS.get(key)
        if prompt_fn is None:
            raise ValueError(f"Unknown fun prompt key: '{key}'. Check prompts.py.")
    else:
        raise ValueError(f"Unknown MODE: '{MODE}'. Use 'headshot' or 'fun'.")

    prompt = prompt_fn(TRIGGER_WORD)

    # Apply preset
    preset_kwargs = PRESETS.get(PRESET, {})

    # Output folder
    folder = Path("outputs") / f"{MODE}_{key}_{_sanitize(_short_label(prompt))}"
    folder.mkdir(parents=True, exist_ok=True)

    print(f"\nMode    : {MODE} / {key}")
    print(f"Preset  : {PRESET}  {preset_kwargs}")
    print(f"Seed    : {FIXED_SEED or 'random'}")
    print(f"Outputs : {NUM_OUTPUTS}")
    print(f"Folder  : {folder}\n")

    used_seed, urls = generate(
        prompt,
        seed=FIXED_SEED,
        num_outputs=NUM_OUTPUTS,
        **preset_kwargs,
    )

    print(f"Seed used: {used_seed}")

    # Log seed + prompt for reproducibility
    with open(folder / "session.log", "a") as log:
        log.write(
            f"seed={used_seed}  preset={PRESET}  mode={MODE}/{key}\n"
            f"prompt:\n{prompt}\n"
            + "-" * 60 + "\n"
        )

    # Download images
    for i, url in enumerate(urls, start=1):
        print(f"Downloading {i}/{len(urls)}...")
        download_image(url, folder, i)

    print(f"\nDone. Images saved to: {folder}")
