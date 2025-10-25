import random

# Playful human touches
PHRASES = [
    "you know what I mean?",
    "and here’s the kicker:",
    "let’s be real for a sec—",
    "funny thing is,",
    "you won’t believe this but",
    "the wild part is,",
]

# Hook words to grab attention
HOOKS = [
    "🔥 Boom!",
    "👉 Here’s the deal:",
    "💡 Think about it—",
    "✨ Picture this:",
    "😅 Real talk:",
]

# Relatable metaphors/examples
ANALOGIES = [
    "It’s like teaching an old dog new tricks.",
    "Think of it like giving your brain a turbo boost.",
    "It’s almost like coffee for your ideas.",
    "Imagine planting a tiny seed that grows into a huge tree—that’s what’s happening here.",
]


def vibe_enhancer(text: str) -> str:
    """Add human vibe: hooks, fun phrases, and analogies."""
    # Randomly add hook at start
    if random.random() < 0.4:
        text = f"{random.choice(HOOKS)} {text}"

    # Sprinkle in a phrase
    if random.random() < 0.5:
        text = f"{text} {random.choice(PHRASES)}"

    # Occasionally add an analogy
    if random.random() < 0.5:
        text = f"{text} {random.choice(ANALOGIES)}"

    return text