import random

METAPHORS = [
    "It's kind of like teaching a puppy new tricks.",
    "Think of it as tuning a musical instrument until it sounds right.",
    "It works like gardeners pruning branches to help trees grow healthier."
]

def originality_boost(text: str) -> str:
    """
    Add a creative twist / metaphor at the end of text
    """
    return f"{text} {random.choice(METAPHORS)}"