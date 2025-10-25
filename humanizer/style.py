import random
import textstat

# Conversational connectors
CASUAL_TRANSITIONS = ["Anyway,", "You know,", "Like,", "Honestly,"]
FORMAL_TRANSITIONS = ["Furthermore,", "In addition,", "Moreover,", "On the other hand,"]
PLAYFUL_TRANSITIONS = ["Guess what?", "Ta-da!", "Boom!", "You won’t believe this, but..."]


def style_polish(text: str, tone: str = "neutral") -> str:
    """
    Polishes text style depending on tone (casual, formal, playful).
    Adds connectors if readability is too rigid.
    """
    score = textstat.flesch_reading_ease(text)

    if tone == "casual":
        transitions = CASUAL_TRANSITIONS
    elif tone == "formal":
        transitions = FORMAL_TRANSITIONS
    elif tone == "playful":
        transitions = PLAYFUL_TRANSITIONS
    else:
        transitions = []  # neutral: no extra transitions

    # Add transitional phrase if text is too stiff/academic
    if score < 50 and transitions:
        return f"{random.choice(transitions)} {text}"
    return text