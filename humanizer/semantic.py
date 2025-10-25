import random
from transformers import pipeline

# Load the model once
_paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

def semantic_rewrite(text: str) -> str:
    """
    Rephrase text while keeping meaning.
    Now supports multiple variations using sampling.
    """
    results = _paraphraser(
        f"paraphrase: {text}",
        num_return_sequences=3,   # multiple outputs
        max_length=128,
        do_sample=True,           # <-- THIS enables sampling (fix!)
        top_k=50,                 # choose from top 50 candidates
        top_p=0.95,               # nucleus sampling
        temperature=0.9           # balance creativity vs coherence
    )
    return random.choice([r['generated_text'] for r in results])