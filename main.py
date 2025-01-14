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

# Apply modern dark theme with improved colors
st.set_page_config(page_title="Decorative House Item Generator", layout="wide")
st.markdown("""
    <style>
        /* General App Styling */
        .stApp {
            background-color: #121212; /* Deep Charcoal */
            color: #e0e0e0; /* Light Gray */
        }

        /* Title Styling */
        .stTitle {
            color: #ffffff; /* White */
            text-align: center;
            font-family: 'Helvetica Neue', sans-serif;
        }

        /* Card Styling */
        .card {
            background-color: #1e1e1e; /* Slightly Lighter Charcoal */
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
            transition: transform 0.2s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        /* Sidebar Styling */
        .sidebar .sidebar-content {
            background-color: #1f1f1f; /* Dark Gray */
            color: #e0e0e0;
        }

        /* Buttons Styling */
        .css-1emrehy.edgvbvh3 {
            background-color: #6200ea; /* Vibrant Purple */
            color: #ffffff;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        .css-1emrehy.edgvbvh3:hover {
            background-color: #3700b3; /* Darker Purple on Hover */
        }

        /* Select Box Styling */
        .css-2b097c-container {
            background-color: #2c2c2c;
            color: #ffffff;
        }

        .css-1pahdxg-control {
            background-color: #2c2c2c;
            border: 1px solid #6200ea;
            border-radius: 8px;
        }

        .css-yk16xz-control:hover {
            border-color: #3700b3;
        }

        .css-1okebmr-indicatorSeparator {
            background-color: #6200ea;
        }

        /* Links Styling */
        a {
            color: #bb86fc; /* Soft Purple */
        }

        /* Lists Styling */
        ul {
            list-style-type: square;
            padding-left: 20px;
        }

        /* Header Styling */
        h3, h4 {
            color: #bb86fc; /* Soft Purple */
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
            <h3>Selection {st.session_state.selected_history_index + 1}</h3>
            <div style="display: flex; gap: 20px;">
                <div>
                    <p><b>Category:</b> {selected_item['category']}</p>
                    <p><b>Type:</b> {selected_item['type']}</p>
                </div>
                <div>
                    <p><b>Look:</b> {selected_item['look']}</p>
                    <p><b>Feel:</b> {selected_item['feel']}</p>
                </div>
            </div>
            <div>
                <p><b>Adjectives:</b></p>
                <ul>
                    {''.join([f'<li>{key}: {value}</li>' for key, value in selected_item['adjective'].items()])}
                </ul>
                <p><b>Vibe:</b> {selected_item['vibe']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

# Selection method
method = st.radio("Choose a selection method:", ["Manual", "Random"], horizontal=True)

if method == "Manual":
    selected_category = st.selectbox("Select a category:", list(types.keys()))
    selected_type = st.selectbox("Select a type:", types[selected_category])
    selected_adjective = {key: st.selectbox(f"Select {key}:", values) for key, values in adjectives.items()}
    selected_look = st.selectbox("Select a look:", list(looks.keys()))
    selected_feel = st.selectbox("Select a feel:", list(feels.keys()))
    selected_vibe = st.selectbox("Select a vibe:", list(vibes.keys()))

    if st.button("Save Selection"):
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
                <div style="display: flex; gap: 20px;">
                    <div>
                        <p><b>Category:</b> {last_random['category']}</p>
                        <p><b>Type:</b> {last_random['type']}</p>
                    </div>
                    <div>
                        <p><b>Look:</b> {last_random['look']}</p>
                        <p><b>Feel:</b> {last_random['feel']}</p>
                    </div>
                </div>
                <div>
                    <p><b>Adjectives:</b></p>
                    <ul>
                        {''.join([f'<li>{key}: {value}</li>' for key, value in last_random['adjective'].items()])}
                    </ul>
                    <p><b>Vibe:</b> {last_random['vibe']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
