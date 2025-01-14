import streamlit as st
import random

# Dictionaries for the categories
types = {
    "wall_decor": ["painting", "tapestry", "mirror", "wall clock"],
    "table_decor": ["vase", "candle holder", "ornament", "bookend", "tray"],
    "lighting": ["lamp", "lantern", "chandelier", "string lights", "sconce"],
    "soft_decor": ["throw pillow", "blanket", "rug", "curtain", "bean bag"],
    "functional_decor": ["planter", "key holder", "coat rack", "jewelry box"],
    "art_pieces": ["sculpture", "figurine", "abstract art", "statue", "relief art"],
    "seasonal_decor": ["Christmas tree", "pumpkin", "wreath", "garland"],
    "other": ["room divider", "decorative basket", "accent furniture", "clock"]
}

adjectives = {
    "size": ["tiny", "small", "medium", "large", "oversized"],
    "shape": ["round", "square", "rectangular", "triangular", "irregular"],
    "material": ["wooden", "metallic", "ceramic", "glass", "woven", "plastic", "stone"],
    "color": ["vibrant", "pastel", "neutral", "monochrome", "gradient"],
    "finish": ["glossy", "matte", "polished", "textured", "aged", "distressed"],
    "decorative_detail": ["patterned", "plain", "engraved", "painted", "studded"],
    "theme_specific": ["geometric", "floral", "abstract", "nature-inspired", "minimalist"]
}

looks = {
    "modern": ["sleek", "minimalist", "clean lines"],
    "traditional": ["ornate", "detailed", "classic"],
    "rustic": ["raw", "weathered", "earthy"],
    "industrial": ["metallic", "rough", "functional"],
    "vintage": ["antique", "faded", "nostalgic"],
    "eclectic": ["mixed", "bohemian", "vibrant"],
    "luxurious": ["opulent", "rich", "elegant"],
    "artistic": ["creative", "unique", "expressive"]
}

feels = {
    "warm": ["inviting", "cozy", "homely"],
    "cool": ["refreshing", "calm", "serene"],
    "dynamic": ["energetic", "bold", "vivid"],
    "relaxing": ["soothing", "tranquil", "peaceful"],
    "inspiring": ["uplifting", "motivating", "visionary"],
    "playful": ["fun", "whimsical", "quirky"]
}

vibes = {
    "coastal": ["beachy", "light", "airy"],
    "bohemian": ["layered", "colorful", "free-spirited"],
    "urban": ["contemporary", "edgy", "chic"],
    "nature": ["organic", "earthy", "green"],
    "romantic": ["soft", "dreamy", "elegant"],
    "adventurous": ["bold", "dramatic", "exploratory"],
    "festive": ["bright", "joyful", "celebratory"]
}

# Function to generate random selections
def generate_random():
    selected_type = random.choice(list(types.keys()))
    selected_adjective = {key: random.choice(values) for key, values in adjectives.items()}
    selected_look = random.choice(list(looks.keys()))
    selected_feel = random.choice(list(feels.keys()))
    selected_vibe = random.choice(list(vibes.keys()))
    return selected_type, selected_adjective, selected_look, selected_feel, selected_vibe

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit app UI
st.title("Decorative House Item Generator")
st.write("Generate decorative house item designs by selecting categories manually or randomly!")

# Selection method
method = st.radio("Choose a selection method:", ["Manual", "Random"])

if method == "Manual":
    selected_type = st.selectbox("Select a type:", list(types.keys()))
    selected_adjective = {key: st.selectbox(f"Select {key}:", values) for key, values in adjectives.items()}
    selected_look = st.selectbox("Select a look:", list(looks.keys()))
    selected_feel = st.selectbox("Select a feel:", list(feels.keys()))
    selected_vibe = st.selectbox("Select a vibe:", list(vibes.keys()))

    if st.button("Save Selection"):
        st.session_state.history.append({
            "type": selected_type,
            "adjective": selected_adjective,
            "look": selected_look,
            "feel": selected_feel,
            "vibe": selected_vibe
        })

elif method == "Random":
    if st.button("Generate Random Selection"):
        selected_type, selected_adjective, selected_look, selected_feel, selected_vibe = generate_random()
        st.session_state.history.append({
            "type": selected_type,
            "adjective": selected_adjective,
            "look": selected_look,
            "feel": selected_feel,
            "vibe": selected_vibe
        })

    if st.session_state.history:
        st.write(f"### Last Random Selection:")
        last_random = st.session_state.history[-1]
        st.write(f"- **Type:** {last_random['type']}")
        for key, value in last_random['adjective'].items():
            st.write(f"- **{key.capitalize()}:** {value}")
        st.write(f"- **Look:** {last_random['look']}")
        st.write(f"- **Feel:** {last_random['feel']}")
        st.write(f"- **Vibe:** {last_random['vibe']}")

# Display history
if st.session_state.history:
    st.write("### Selection History:")
    for i, item in enumerate(st.session_state.history, 1):
        st.write(f"#### Selection {i}:")
        st.write(f"- **Type:** {item['type']}")
        for key, value in item['adjective'].items():
            st.write(f"- **{key.capitalize()}:** {value}")
        st.write(f"- **Look:** {item['look']}")
        st.write(f"- **Feel:** {item['feel']}")
        st.write(f"- **Vibe:** {item['vibe']}")
