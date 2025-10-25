import random

def apply_persona(text: str, persona: str = "neutral") -> str:
    """
    Reshape text style depending on persona.
    - teacher: explanatory, structured, guiding
    - blogger: chatty, engaging, catchy
    - mentor: encouraging, thoughtful, inspiring
    - storyteller: vivid, narrative, metaphorical
    """
    if persona == "teacher":
        additions = [
            "Let’s break this down step by step.",
            "Think of this as an important concept to carry forward.",
            "The key takeaway here is clarity."
        ]
        return f"{text} {random.choice(additions)}"

    elif persona == "blogger":
        additions = [
            "Pretty wild, right?",
            "This is the kind of stuff you’ll want to share with a friend.",
            "And honestly—that’s the fun part!"
        ]
        return f"{text} {random.choice(additions)}"

    elif persona == "mentor":
        additions = [
            "Remember—you’ve got this.",
            "Growth doesn’t happen overnight, but this is a step forward.",
            "What matters most is applying this with confidence."
        ]
        return f"{text} {random.choice(additions)}"

    elif persona == "storyteller":
        additions = [
            "It’s almost like sitting around a fire, passing down a tale.",
            "Imagine this as the beginning of a journey.",
            "And just like any great story, there’s a twist waiting ahead."
        ]
        return f"{text} {random.choice(additions)}"

    else:  # neutral fallback
        return text