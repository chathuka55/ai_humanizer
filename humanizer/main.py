from .semantic import semantic_rewrite
from .style import style_polish
from .originality import originality_boost
from .vibe import vibe_enhancer

def humanizer_pipeline(text: str, tone: str = "neutral", vibe: bool = True) -> str:
    """
    Full humanizer pipeline:
    1. Semantic rewrite
    2. Tone-aware polish
    3. Optional vibe enhancement (catchy hooks/phrases)
    4. Originality boost
    """
    t1 = semantic_rewrite(text)
    t2 = style_polish(t1, tone=tone)
    if vibe:
        t2 = vibe_enhancer(t2)
    t3 = originality_boost(t2)
    return t3