"""
All prompts for flux-lora-headshots.

Replace YOUR_NAME with your LoRA trigger word everywhere before running.
"""

# ---------------------------------------------------------------------------
# HEADSHOT PROMPTS
# ---------------------------------------------------------------------------

HEADSHOT_PROMPTS = {

    "corporate": lambda name: f"""Portrait of {name}, {name} — exact likeness, same person, recognizable; no other face, match the trained subject.
Professional corporate headshot, confident and charismatic, expressive, not too serious. Lips closed or slight smile; no half-open mouth, no parted lips.
Wearing a tailored dark suit and crisp white shirt.
Full head visible, entire head within frame, no cropping of head or hair. Classic headshot: head, shoulders, upper chest in frame; medium close-up, face does not dominate. Face proportioned correctly — neither too large nor too small.
Clear features, natural skin, impeccable grooming; very lean, low body fat, defined jawline, chiseled cheekbones, athletic build.
Studio lighting, soft highlights, catch lights in eyes, shallow depth of field, sharp focus on face.
Neutral blurred background, solid gray or beige, no objects. Camera 30–45° off-center, three-quarter view, eye contact.
8K, photorealistic, professional color grading.""",

    "corporate_serious": lambda name: f"""A hyper-realistic, professional high-end corporate headshot portrait of {name},
a real man exuding confidence, determination, and quiet charisma.
Expression: serious yet approachable — neutral with relaxed eyes and a calm, composed demeanor. No smile, no frown. Eyebrows relaxed and natural.
Camera angle 30–45° off-center, three-quarter view, clear eye contact. Shoulders visible; face fills the frame appropriately.
Wearing a tailored modern dark suit with a crisp white shirt — polished, executive-level attire.
Facial features sharp, clear, lifelike: natural skin tones, impeccable grooming, realistic texture (pores, stubble if applicable). Physique appears strong and athletic.
Studio lighting: soft balanced highlights, catch lights in the eyes, realistic shallow depth of field — face sharply focused, background perfectly blurred.
Background: sober, simple, neutral solid color (soft gray, beige, or dark charcoal) — no objects, no textures, no patterns.
8K UHD, photorealistic masterpiece, professional color grading, contemporary corporate aesthetic, lifelike textures.""",

    "corporate_young": lambda name: f"""A hyper-realistic, professional high-end corporate headshot photoshoot of {name},
a real man who is confident, inspiring and very charismatic, not too serious — he is 25 years old, make sure he looks young.
{name} is wearing a tailored modern sleek dark suit with crisp white shirt.
The image features clear facial features, natural skin tones, and impeccable grooming.
The face has to fit in the frame, shoulders should be visible. The man is lean and muscular.
Studio lighting: soft balanced highlights, catch lights in the eyes, realistic shallow depth of field, sharp focus on face.
Background: sober, simple, neutral solid color — no objects, no textures, no patterns. Clean, minimalist, distraction-free.
8K UHD masterpiece, masterful photography, professional color grading, contemporary aesthetic, lifelike textures.
Camera angle between straight frontal and three-quarter side view (approx. 30–45° off-center), clear eye contact with the viewer.""",

    "casual": lambda name: f"""A hyper-realistic photoshoot of {name}, {name} — exact likeness, same person, recognizable.
A charismatic 25-year-old man, confident smirk, casual yet classy outfit, tight-fitting to show an athletic build.
Wearing a well-fitted shirt or casual blazer with a tailored pair of trousers.
Clear facial features, natural skin tones, impeccable grooming.
Shot during golden hour, warm skin tones, natural lighting, no flash, subject in sharp focus, bokeh background.
Shallow depth of field, professional color grading, contemporary aesthetic, lifelike textures.
8K, photorealistic.""",
}

# ---------------------------------------------------------------------------
# FUN / MEME PROMPTS (close-up, face fills frame)
# ---------------------------------------------------------------------------

FUN_PROMPTS = {

    "npc": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, straight-on close-up.
Completely blank, deadpan NPC expression — eyes slightly glazed, mouth neutral, no emotion.
Flat office or neutral background, even lighting like a default character select screen.
Photorealistic, 8K, sharp on face, uncanny funny vibe, 2026 meme style.""",

    "touch_grass": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, tight crop on face and upper shoulders.
Looking at camera with exaggerated "I just touched grass" unbothered smirk, slight side-eye, one eyebrow raised.
Soft outdoor golden-hour light on face, grass slightly visible in bokeh behind.
Photorealistic, 8K, sharp focus on face, catch lights in eyes, funny 2026 meme energy.""",

    "main_character": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, dramatic three-quarter close-up.
Looking away from camera with main-character energy, wind in hair, soft cinematic lighting.
Expression: confident, slightly delulu, like they just had a plot twist.
Photorealistic, 8K, shallow depth of field, face sharp, background blurred, trendy 2026 aesthetic.""",

    "rizz": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, close-up with slight tilt, confident angle.
Smirking at camera with maximum rizz — half smile, raised eyebrow, eyes locked on viewer.
Warm low-key lighting, catch lights in eyes, shallow depth of field.
Photorealistic, 8K, sharp focus on face, funny charismatic 2026 portrait.""",

    "side_eye": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, three-quarter close-up.
Giving heavy side-eye to the camera — one eye cut toward viewer, unimpressed expression, slight smirk.
Neutral or soft background, studio-style lighting on face.
Photorealistic, 8K, sharp on face, catch lights, 2026 funny judgmental vibe.""",

    "unhinged": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, tight close-up.
Wide unhinged grin at camera — slightly too much teeth, crazy happy eyes, unhinged but funny energy.
Bright even lighting, clean background, face sharp and expressive.
Photorealistic, 8K, shallow depth of field, 2026 chaotic meme portrait.""",

    "delulu": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, soft close-up.
Staring at camera with delulu hopeful expression — wide innocent eyes, small dreamy smile, believing in the delusion.
Soft diffused lighting, slight glow, dreamy bokeh background.
Photorealistic, 8K, sharp focus on face, 2026 delulu aesthetic, funny and wholesome.""",

    "no_thoughts": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, frontal close-up.
Completely vacant expression — mouth slightly open, eyes unfocused, zero thoughts head empty.
Plain neutral background, flat soft light, face sharp.
Photorealistic, 8K, funny blank 2026 meme face, relatable.""",

    "plot_twist": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, dramatic close-up.
Exaggerated plot-twist shock — eyes wide, jaw dropped, OMG expression.
Dramatic lighting from one side, shallow depth of field, face sharp.
Photorealistic, 8K, catch lights in eyes, 2026 reaction meme, funny over-the-top.""",

    "slay": lambda name: f"""Close-up portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} face fills the frame, glam close-up, slight low angle.
Unbothered slay expression — cool gaze at camera, slight smirk, flawless main-character energy.
Soft glam lighting, clean blurred background, catch lights in eyes.
Photorealistic, 8K, sharp on face, 2026 slay aesthetic, funny and iconic.""",

    "medieval_knight": lambda name: f"""Portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} as a medieval knight in shining armor, holding a sword, standing in a castle courtyard,
dramatic lighting, photorealistic, 8K, epic fantasy portrait.""",

    "superhero": lambda name: f"""Portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} as a superhero in a colorful costume, cape flowing,
flying through the sky, city below, dramatic lighting, photorealistic, 8K, epic superhero portrait.""",

    "astronaut": lambda name: f"""Portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} floating in space, friendly aliens in the background, Earth below,
space suit with helmet, photorealistic, 8K, sci-fi cinematic lighting.""",

    "80s": lambda name: f"""Portrait of {name}, {name} — exact likeness, same person, recognizable.
{name} in 1980s style, big hair, neon colors,
arcade background, retro aesthetic, photorealistic, 8K, nostalgic portrait.""",
}

# ---------------------------------------------------------------------------
# DEFAULT SELECTIONS
# ---------------------------------------------------------------------------

DEFAULT_HEADSHOT = "corporate"
DEFAULT_FUN = "npc"
