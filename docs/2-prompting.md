# Prompting Guide

How to get the best headshots from your Flux LoRA.

---

## The golden rules

### 1. Lead with identity, repeat the trigger word

Put your trigger word first and repeat it at least twice. This forces the model to anchor on your face before it builds the scene.

```text
Portrait of JOHN, JOHN — exact likeness, same person, recognizable...
```

Without this, the model tends to generate a "generic headshot face" and paste your LoRA on top — which is the "pasted" look.

### 2. Remove generic dataset phrases

These phrases push the model toward averaged stock-photo faces:

- `Base your render on a diverse dataset of professional portraits` — **remove this**
- `masterpiece` — weakens identity, adds stock-photo tendencies
- `8k UHD masterpiece` — keep `8K, photorealistic` but drop `masterpiece`

### 3. Keep the prompt focused

Long, competing cues (lighting + angle + outfit + skin + background + camera specs) make it harder for the LoRA identity to come through. Pick the details that matter most and cut the rest.

### 4. Describe what you DON'T want

Negative phrasing in the prompt itself works well for Flux:

```text
Lips closed or slight smile; no half-open mouth, no parted lips.
Neutral blurred background — no objects, no textures, no patterns.
```

---

## Prompt anatomy (corporate headshot)

```text
[IDENTITY]      Portrait of NAME, NAME — exact likeness, same person, recognizable.
[EXPRESSION]    Confident and charismatic, not too serious. Lips closed or slight smile.
[OUTFIT]        Wearing a tailored dark suit and crisp white shirt.
[FRAMING]       Full head visible, shoulders in frame. Medium close-up.
[PHYSICALITY]   Lean, athletic build; defined jawline; natural skin tones.
[LIGHTING]      Studio lighting, soft highlights, catch lights in eyes, shallow depth of field.
[BACKGROUND]    Neutral blurred background, solid gray or beige, no objects.
[CAMERA]        Camera 30–45° off-center, three-quarter view, eye contact.
[QUALITY]       8K, photorealistic, professional color grading.
```

You don't need all of these. The `corporate` preset in `prompts.py` covers the full version; start there and trim if results feel over-constrained.

---

## Choosing your prompt key

### For professional use (LinkedIn, CV, website)

| Key | Use it when... |
| --- | --- |
| `corporate` | You want the classic LinkedIn headshot — suit, confident, athletic |
| `corporate_serious` | You need something more formal / executive |
| `corporate_young` | You're ~25 and the suit makes you look too old |
| `casual` | You want something warmer, social media–ready |

### For fun / social

All fun prompts use a close-up framing where the face fills the frame. They work best with the `balanced` or `identity` preset.

| Key | Vibe |
| --- | --- |
| `npc` | Deadpan blank face — great for memes |
| `rizz` | Charismatic half-smirk |
| `main_character` | Cinematic, slightly dramatic |
| `side_eye` | Judgmental, unimpressed |
| `unhinged` | Wide grin, chaotic energy |
| `delulu` | Wide hopeful eyes, dreamy |
| `no_thoughts` | Vacant stare, head empty |
| `plot_twist` | Exaggerated shock |
| `slay` | Unbothered, cool, glam |
| `medieval_knight` | Fantasy armor |
| `superhero` | Cape, city below |
| `astronaut` | Space suit, aliens |
| `80s` | Neon, big hair, arcade |

---

## Seed control

A seed locks the composition — same seed + same prompt = same framing every time.

```python
# In generate.py
FIXED_SEED = 65658157   # known-good seed for corporate framing
```

**When to fix the seed:**

- You found a great framing and want to iterate on prompt/preset only
- You're generating a batch for the same headshot style

**When to leave it random (`None`):**

- First exploration run — let the model explore compositions
- Fun prompts where variety is the point

Once you find a seed you like, note it down and use it for all variations of that session.

---

## Writing your own prompts

You can add new prompts directly in `prompts.py`. The pattern is a lambda that takes the trigger word:

```python
HEADSHOT_PROMPTS["outdoor"] = lambda name: f"""Portrait of {name}, {name} — exact likeness.
{name} standing outdoors in natural daylight, relaxed confident stance.
Casual smart outfit, open-collar shirt. Bokeh background of trees or architecture.
Photorealistic, 8K, natural color grading."""
```

Then set `PROMPT_KEY = "outdoor"` in `generate.py`.

---

## Post-processing (optional)

Flux + LoRA output is already high quality. Post-processing is optional but can help:

- **Eyes**: If eyes look slightly off, a touch-up in Photoshop or Lightroom is fast
- **Skin**: The output is already realistic — avoid heavy AI retouching that erases texture
- **Background swap**: Use any background removal tool if you need a different background
- **Upscaling**: Not needed for 1024×1024 PNG outputs at 50 steps — already print-quality
