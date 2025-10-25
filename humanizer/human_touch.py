import random
import re

# Natural human expressions & fillers
EXPRESSIONS = [
    "At the end of the day,",
    "What this really means is",
    "If we’re being honest,",
    "Here’s the real deal:",
    "The truth is,"
]

REFLECTIVE_CUES = [
    "Think about how this connects to everyday life.",
    "It’s something we can all relate to, in one way or another.",
    "That’s not just theory—it’s reality playing out in real time.",
    "And this is where it hits close to home."
]

def smooth_flow(text: str) -> str:
    """Break long sentences into smaller, readable parts (like humans do)."""
    sentences = re.split(r'(?<=[.?!]) +', text)
    new_sents = []
    for s in sentences:
        if len(s.split()) > 18:  # too long
            mid = len(s.split()) // 2
            words = s.split()
            new_sents.append(" ".join(words[:mid]) + ".")
            new_sents.append(" ".join(words[mid:]))
        else:
            new_sents.append(s)
    return " ".join(new_sents)

def add_expressions(text: str) -> str:
    """Sprinkle natural expressions and reflective cues."""
    # Add opening expression sometimes
    if random.random() < 0.4:
        text = f"{random.choice(EXPRESSIONS)} {text}"

    # Add reflective cue sometimes
    if random.random() < 0.4:
        text = f"{text} {random.choice(REFLECTIVE_CUES)}"

    return text

def humanize_text(text: str) -> str:
    """Human-touch layer: smoother flow + human expressions."""
    text = smooth_flow(text)
    text = add_expressions(text)
    return text