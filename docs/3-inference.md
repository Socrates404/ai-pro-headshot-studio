# Inference Parameter Reference

When the face looks like a **generic base model + LoRA pasted on top** and doesn't look like the person, these are the levers to pull. Use them together.

---

## Quick test order (start here)

1. Use `PRESET = "identity"` + simplified prompt (no "diverse dataset", identity first)
2. Nudge `guidance_scale`: 1.5 → 2.0 → 2.5
3. Nudge `lora_scale`: 0.85 → 0.9 → 1.0
4. Only try `num_inference_steps = 60` if the face is almost right but slightly "unfinished"

---

## Presets

Set `PRESET` in `generate.py`. These are defined in the `PRESETS` dict:

| Preset | `guidance_scale` | `prompt_strength` | `lora_scale` | Best for |
| --- | --- | --- | --- | --- |
| `identity` | 1.5 | 0.8 | 0.9 | Most recognizable face; least "pasted" |
| `balanced` | 1.75 | 0.9 | 1.1 | Best overall; recommended default |
| `consistent` | 2.0 | 0.85 | 1.0 | Stable framing and head size across runs |
| `2025` | 3.0 | 0.8 | 1.0 | Previous best; more prompt-driven |

---

## Parameters explained

### `guidance_scale`

Controls how strongly the **text prompt** steers the image.

- **Too high** (3.5+): model locks onto "professional headshot, suit, studio…" → generates a generic executive face first. LoRA has to fight that structure → "pasted" feel.
- **Too low** (< 1.5): image can get soft or incoherent; structure is weak.

**Sweet spot for face LoRAs: 1.5 – 2.5**

```python
# Try in this order if face doesn't look like you:
guidance_scale = 1.5   # identity preset — LoRA has most say
guidance_scale = 2.0   # consistent preset — balanced
guidance_scale = 2.5   # still identity-friendly but more prompt structure
```

---

### `prompt_strength`

How much the prompt dictates the final result. At 1.0 the prompt has maximum influence.

A long, detailed prompt (suit, lighting, angle, "diverse dataset", "8k", etc.) can **anchor the model to a stock-photo face**. The LoRA then only adjusts on top of that.

**Recommended: 0.8 – 0.85**

```python
prompt_strength = 0.8   # default — LoRA has good say
prompt_strength = 0.75  # if face still feels dominated by "generic corporate headshot"
prompt_strength = 0.85  # if identity is good but pose/lighting get too random
```

---

### `lora_scale`

Strength of the LoRA versus the base model.

- **1.0** can give a "sticker on another face" look if the LoRA is strong
- Slightly **below 1.0** often blends identity into the scene instead of overlaying it

**Recommended: 0.85 – 1.1**

```python
lora_scale = 0.9   # more integrated look (start here)
lora_scale = 1.0   # if face is too weak / not recognizable
lora_scale = 1.1   # if you want stronger identity dominance
lora_scale = 0.85  # if it looks like a mask or texture pasted on
```

---

### `num_inference_steps`

More steps = more refinement, more cost.

**Default: 50** — don't go lower for final outputs.

Try 60–70 only if the face is almost right but "unfinished" looking. Going above 70 rarely helps with Flux.

---

### `go_fast`

- `False` (default): uses bf16 precision — better quality
- `True`: uses fp8 — faster but slightly lower quality

Use `go_fast=True` only for cheap test runs where you're checking composition, not final quality.

---

### `output_format` and `output_quality`

- `output_format="png"`, `output_quality=100` — lossless, maximum detail (default)
- `output_format="jpg"`, `output_quality=80` — faster downloads, fine for previews

Always use PNG for anything you'll actually use.

---

## The "pasted face" checklist

If the output looks like a real person wearing your face as a mask:

- [ ] Lower `guidance_scale` to 1.5 (`identity` preset)
- [ ] Lower `lora_scale` to 0.85 or 0.9
- [ ] Put trigger word first in the prompt, repeat it twice
- [ ] Remove "Base your render on a diverse dataset of professional portraits" from the prompt
- [ ] Shorten the prompt — fewer competing cues
- [ ] Add "exact likeness, same person, recognizable" near the trigger word

## The "blurry/incoherent face" checklist

If the face doesn't have clear features:

- [ ] Raise `guidance_scale` to 2.5 or 3.0
- [ ] Raise `prompt_strength` to 0.85
- [ ] Increase `num_inference_steps` to 60
- [ ] Make sure `go_fast=False`
- [ ] Use `output_format="png"`, `output_quality=100`
