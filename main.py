import streamlit as st
import random

# Dictionaries for the categories
types = {
    "Wall Decor": ["Painting", "Tapestry", "Mirror", "Wall Clock"],
    "Table Decor": ["Vase", "Candle Holder", "Ornament", "Bookend", "Tray"],
    "Lighting": ["Lamp", "Lantern", "Chandelier", "String Lights", "Sconce"],
    "Soft Decor": ["Throw Pillow", "Blanket", "Rug", "Curtain", "Bean Bag"],
    "Functional Decor": ["Planter", "Key Holder", "Coat Rack", "Jewelry Box"],
    "Art Pieces": ["Sculpture", "Figurine", "Abstract Art", "Statue", "Relief Art"],
    "Seasonal Decor": ["Christmas Tree", "Pumpkin", "Wreath", "Garland"],
    "Other": ["Room Divider", "Decorative Basket", "Accent Furniture", "Clock"]
}

adjectives = {
    "Size": ["Tiny", "Small", "Medium", "Large", "Oversized"],
    "Shape": ["Round", "Square", "Rectangular", "Triangular", "Irregular"],
    "Material": ["Wooden", "Metallic", "Ceramic", "Glass", "Woven", "Plastic", "Stone"],
    "Color": ["Vibrant", "Pastel", "Neutral", "Monochrome", "Gradient"],
    "Finish": ["Glossy", "Matte", "Polished", "Textured", "Aged", "Distressed"],
    "Decorative Detail": ["Patterned", "Plain", "Engraved", "Painted", "Studded"],
    "Theme Specific": ["Geometric", "Floral", "Abstract", "Nature-Inspired", "Minimalist"]
}

looks = {
    "Modern": ["Sleek", "Minimalist", "Clean Lines"],
    "Traditional": ["Ornate", "Detailed", "Classic"],
    "Rustic": ["Raw", "Weathered", "Earthy"],
    "Industrial": ["Metallic", "Rough", "Functional"],
    "Vintage": ["Antique", "Faded", "Nostalgic"],
    "Eclectic": ["Mixed", "Bohemian", "Vibrant"],
    "Luxurious": ["Opulent", "Rich", "Elegant"],
    "Artistic": ["Creative", "Unique", "Expressive"]
}

feels = {
    "Warm": ["Inviting", "Cozy", "Homely"],
    "Cool": ["Refreshing", "Calm", "Serene"],
    "Dynamic": ["Energetic", "Bold", "Vivid"],
    "Relaxing": ["Soothing", "Tranquil", "Peaceful"],
    "Inspiring": ["Uplifting", "Motivating", "Visionary"],
    "Playful": ["Fun", "Whimsical", "Quirky"]
}

vibes = {
    "Coastal": ["Beachy", "Light", "Airy"],
    "Bohemian": ["Layered", "Colorful", "Free-Spirited"],
    "Urban": ["Contemporary", "Edgy", "Chic"],
    "Nature": ["Organic", "Earthy", "Green"],
    "Romantic": ["Soft", "Dreamy", "Elegant"],
    "Adventurous": ["Bold", "Dramatic", "Exploratory"],
    "Festive": ["Bright", "Joyful", "Celebratory"]
}

# Function to generate random selections
def generate_random():
    selected_category = random.choice(list(types.keys()))
    selected_type = random.choice(types[selected_category])
    selected_adjective = {key: random.choice(values) for key, values in adjectives.items()}
    selected_look = random.choice(list(looks.keys()))
    selected_feel = random.choice(list(feels.keys()))
    selected_vibe = random.choice(list(vibes.keys()))
    return selected_category, selected_type, selected_adjective, selected_look, selected_feel, selected_vibe

# Initialize session state for history and selected history
if "history" not in st.session_state:
    st.session_state.history = []
if "selected_history_index" not in st.session_state:
    st.session_state.selected_history_index = None

# Optional: Minimal CSS for card styling in light mode
st.markdown("""
    <style>
        .card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 4px 4px 16px rgba(0, 0, 0, 0.2);
        }

        .header {
            font-size: 1.5em;
            margin-bottom: 10px;
            color: #333333;
        }

        .subheader {
            font-size: 1.2em;
            margin-bottom: 8px;
            color: #555555;
        }

        .list-item {
            color: #666666;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app UI
st.title("Decorative House Item Generator")
st.write("Generate decorative house item designs by selecting categories manually or randomly!")

# Sidebar for selection history
st.sidebar.title("Selection History")
if st.session_state.history:
    for i, item in enumerate(st.session_state.history, 1):
        if st.sidebar.button(f"Selection {i}", key=f"history_{i}"):
            st.session_state.selected_history_index = i - 1

# Display selected history item in main area
if st.session_state.selected_history_index is not None:
    selected_item = st.session_state.history[st.session_state.selected_history_index]
    st.markdown(f"""
        <div class="card">
            <div class="header">Selection {st.session_state.selected_history_index + 1}</div>
            <div style="display: flex; gap: 40px;">
                <div>
                    <div class="subheader">Category & Type</div>
                    <p><strong>Category:</strong> {selected_item['category']}</p>
                    <p><strong>Type:</strong> {selected_item['type']}</p>
                </div>
                <div>
                    <div class="subheader">Look & Feel</div>
                    <p><strong>Look:</strong> {selected_item['look']}</p>
                    <p><strong>Feel:</strong> {selected_item['feel']}</p>
                </div>
            </div>
            <div>
                <div class="subheader">Adjectives & Vibe</div>
                <p><strong>Adjectives:</strong></p>
                <ul>
                    {''.join([f'<li class="list-item">{key}: {value}</li>' for key, value in selected_item['adjective'].items()])}
                </ul>
                <p><strong>Vibe:</strong> {selected_item['vibe']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

# Selection method
method = st.radio("Choose a selection method:", ["Manual", "Random"], horizontal=True)

if method == "Manual":
    with st.form(key='manual_selection'):
        selected_category = st.selectbox("Select a category:", list(types.keys()))
        selected_type = st.selectbox("Select a type:", types[selected_category])
        selected_adjective = {key: st.selectbox(f"Select {key}:", values) for key, values in adjectives.items()}
        selected_look = st.selectbox("Select a look:", list(looks.keys()))
        selected_feel = st.selectbox("Select a feel:", list(feels.keys()))
        selected_vibe = st.selectbox("Select a vibe:", list(vibes.keys()))
        submit_manual = st.form_submit_button("Save Selection")

    if submit_manual:
        st.session_state.history.append({
            "category": selected_category,
            "type": selected_type,
            "adjective": selected_adjective,
            "look": selected_look,
            "feel": selected_feel,
            "vibe": selected_vibe
        })
        st.success("Selection saved to history!")

elif method == "Random":
    if st.button("Generate Random Selection"):
        selection = generate_random()
        st.session_state.history.append({
            "category": selection[0],
            "type": selection[1],
            "adjective": selection[2],
            "look": selection[3],
            "feel": selection[4],
            "vibe": selection[5]
        })
        st.success("Random selection generated and saved to history!")

    if st.session_state.history:
        last_random = st.session_state.history[-1]
        st.write(f"### Last Random Selection:")
        st.markdown(f"""
            <div class="card">
                <div class="header">Selection {len(st.session_state.history)}</div>
                <div style="display: flex; gap: 40px;">
                    <div>
                        <div class="subheader">Category & Type</div>
                        <p><strong>Category:</strong> {last_random['category']}</p>
                        <p><strong>Type:</strong> {last_random['type']}</p>
                    </div>
                    <div>
                        <div class="subheader">Look & Feel</div>
                        <p><strong>Look:</strong> {last_random['look']}</p>
                        <p><strong>Feel:</strong> {last_random['feel']}</p>
                    </div>
                </div>
                <div>
                    <div class="subheader">Adjectives & Vibe</div>
                    <p><strong>Adjectives:</strong></p>
                    <ul>
                        {''.join([f'<li class="list-item">{key}: {value}</li>' for key, value in last_random['adjective'].items()])}
                    </ul>
                    <p><strong>Vibe:</strong> {last_random['vibe']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
