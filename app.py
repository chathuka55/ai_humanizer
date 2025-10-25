import streamlit as st
from humanizer.main import humanizer_pipeline

st.set_page_config(page_title="AI Humanizer 📝")

st.title("📝 AI Humanizer")
st.write("Transform boring text into catchy, humanized writing with extra vibes ✨")

# User input
user_input = st.text_area("Enter text to humanize:")

# Tone selection
tone = st.selectbox(
    "Select tone:",
    ["neutral", "casual", "formal", "playful"]
)

# Vibe switch
vibe = st.checkbox("Add Catchy Vibes (hooks, phrases, analogies)", value=True)

# Humanize button
if st.button("✨ Humanize"):
    if user_input.strip():
        output = humanizer_pipeline(user_input, tone=tone, vibe=vibe)
        st.subheader(f"✨ Humanized Output ({tone}{' + vibes' if vibe else ''})")
        st.write(output)