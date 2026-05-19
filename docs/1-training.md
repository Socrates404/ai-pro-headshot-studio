# Training Guide — Your Flux LoRA

This guide walks you through training a personal Flux LoRA on Replicate so you can generate headshots of yourself.

**Total cost: ~$2. Total time: ~30 minutes (15 min prep + 15 min training).**

---

## Step 1 — Prepare your photos

This is the most important step. Bad training data = bad results, no matter how good the model is.

### What you need

- **10–20 photos** (minimum 10; more is not always better if quality drops)
- **1024×1024 pixels**, square crop
- **Only your face/head** — no group shots, no other people
- **High quality** — sharp focus, good lighting, no heavy filters

### What makes a good training photo

- **Variety of angles**: straight-on, 3/4 view, slight side profile
- **Variety of lighting**: natural light, indoor, studio-style
- **Variety of expressions**: neutral, slight smile, serious — avoid big open-mouth smiles
- **Head fills the frame**: close-up to mid-bust, no full-body shots
- **Clean backgrounds** preferred but not required

### What to avoid

- Sunglasses or anything covering your face
- Heavy makeup that changes your features
- Low-res, blurry, or heavily compressed images
- Duplicates or near-duplicates (similar angle + expression)
- Group photos cropped to just you (quality degrades)

### Resizing tool

Use [Photopea](https://www.photopea.com) (free, browser-based) to crop and resize to 1024×1024.
Export as PNG or high-quality JPG.

---

## Step 2 — Train on Replicate

Replicate hosts GPU infrastructure and lets you train a Flux LoRA through a simple web UI.

### Recommended trainer

**`replicate/fast-flux-trainer`** — fast, reliable, well-tuned for faces.

Direct link: replicate.com/replicate/fast-flux-trainer/train

### Training settings

| Parameter | Recommended value | Notes |
| --- | --- | --- |
| `trigger_word` | A short unique name (e.g. `JOHN`) | All caps avoids token collisions |
| `training_steps` | `2000` | Sweet spot — less overfits, more underfits |
| `lora_rank` | `32` | Good balance of detail vs. generalization |
| `autocaption` | Off | Use the prefix instead (more control) |
| `autocaption_prefix` | `A photo of JOHN` | Replace JOHN with your trigger word |
| `batch_size` | `4` to `8` | Higher = more stable training; default is fine |

### Step-by-step

1. Go to replicate.com/replicate/fast-flux-trainer/train
2. Create a new model destination (e.g. `yourname/yourname-lora`)
3. Upload your 10–20 photos as a ZIP file
4. Set `trigger_word` to your chosen name (e.g. `JOHN`)
5. Set `training_steps` to `2000`
6. Disable autocaption, set prefix to `A photo of JOHN`
7. Click **Run training** — takes ~10–15 minutes
8. When done, go to your model page and copy the **version hash**

### Getting your MODEL_NAME

After training, your model page URL looks like:

```text
replicate.com/yourname/yourname-lora
```

Click on the latest version. The full version string looks like:

```text
yourname/yourname-lora:abc123def456...long-hash...
```

Paste that into your `.env` as `MODEL_NAME`.

---

## Step 3 — Test your LoRA

Run a quick test before committing to a full generation session:

```python
# In generate.py
TRIGGER_WORD = "JOHN"    # your trigger word
MODE         = "headshot"
PROMPT_KEY   = "corporate"
PRESET       = "identity"  # best for first test — prioritizes face likeness
NUM_OUTPUTS  = 2
```

```bash
python generate.py
```

Check the results in `outputs/`. If the face looks like a generic stock photo rather than you, see the troubleshooting section below.

---

## Troubleshooting

### Face doesn't look like me

- Lower `guidance_scale` — try `identity` preset (1.5)
- Lower `lora_scale` — try 0.85 or 0.9
- Check your trigger word matches exactly what you used during training
- Your LoRA might be overfitting — try an earlier checkpoint if Replicate saved one

### Face is blurry or incoherent

- Increase `guidance_scale` — try `balanced` preset (1.75)
- Make sure `num_inference_steps` is at least 50
- Try `go_fast=False` (default) for full bf16 precision

### Overfitting signs (same face in every image regardless of prompt)

- Your training steps may be too high (3000+ with a small dataset)
- Try retraining with 1500 steps
- Check your training data for too many near-duplicate shots

### Head gets cropped out of frame

- Use `consistent` preset — it has higher guidance to follow the framing prompt more closely
- Use a fixed seed (`FIXED_SEED = 65658157`) known to produce good framing

---

## Alternative trainers

If you prefer a different service:

| Option | Notes |
| --- | --- |
| replicate.com/ostris/flux-dev-lora-trainer | The original Flux LoRA trainer, more config options |
| fal.ai/models/fal-ai/flux-lora-portrait-trainer | Portrait-optimized, slightly different UI |
| FluxGym (local) | Fully free, needs 12–20GB VRAM GPU |

---

## Cost breakdown

| Action | Cost |
| --- | --- |
| 2000 training steps | ~$2 |
| 3000 training steps | ~$3 |
| Generate 4 PNG images | ~$0.10–0.20 |

Replicate billing is per-second of GPU compute. Prices may change — check replicate.com/pricing.
