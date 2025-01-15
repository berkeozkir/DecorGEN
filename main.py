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
def generate_random(selected_category=None):
    category = selected_category if selected_category else random.choice(list(types.keys()))
    type_ = random.choice(types[category])
    adjective = {key: random.choice(values) for key, values in adjectives.items()}
    look = random.choice(list(looks.keys()))
    feel = random.choice(list(feels.keys()))
    vibe = random.choice(list(vibes.keys()))
    return category, type_, adjective, look, feel, vibe

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
            background-color: #ffffff;
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

        /* Sidebar Styling */
        .sidebar .sidebar-content {
            background-color: #f5f5f5; /* Light Gray */
            color: #333333;
        }

        /* Button Styling */
        .css-1emrehy.edgvbvh3 {
            background-color: #007BFF; /* Bootstrap Blue */
            color: #ffffff;
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 14px;
            transition: background-color 0.3s;
            margin-bottom: 5px;
        }

        .css-1emrehy.edgvbvh3:hover {
            background-color: #0056b3; /* Darker Blue on Hover */
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app UI
st.title("Decorative House Item Generator")
st.write("Generate decorative house item designs by selecting categories manually, randomly, or partially!")

# Sidebar for selection history
st.sidebar.title("Selection History")
if st.session_state.history:
    # Display history in reverse chronological order
    for i, item in enumerate(reversed(st.session_state.history), 1):
        # Create a meaningful label using Type and Vibe
        label = f"{item['type']} ({item['vibe']})"
        if st.sidebar.button(label, key=f"history_{len(st.session_state.history)-i}"):
            st.session_state.selected_history_index = len(st.session_state.history) - i

# Display selected history item in main area
if st.session_state.selected_history_index is not None:
    selected_item = st.session_state.history[st.session_state.selected_history_index]
    st.markdown(f"""
        <div class="card">
            <div class="header">{"Recent Selection" if st.session_state.selected_history_index == len(st.session_state.history)-1 else f"Selection #{st.session_state.selected_history_index + 1}"}</div>
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
method = st.radio("Choose a selection method:", ["Manual", "Random", "Custom"], horizontal=True)

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
                <div class="header">Random Selection</div>
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

elif method == "Custom":
    st.subheader("Custom Selection")
    with st.form(key='custom_selection'):
        st.write("Select the attributes you want to set manually. Others will be randomly generated.")

        # Attribute selection checkboxes
        select_category_type = st.checkbox("Set Category & Type")
        select_adjectives = st.checkbox("Set Adjectives")
        select_look = st.checkbox("Set Look")
        select_feel = st.checkbox("Set Feel")
        select_vibe = st.checkbox("Set Vibe")

        # Initialize a dictionary to hold selections
        custom_selection = {}

        # Category & Type
        if select_category_type:
            selected_category_custom = st.selectbox("Select a category:", list(types.keys()), key='custom_category')
            selected_type_custom = st.selectbox("Select a type:", types[selected_category_custom], key='custom_type')
            custom_selection['category'] = selected_category_custom
            custom_selection['type'] = selected_type_custom

        # Adjectives
        if select_adjectives:
            st.markdown("**Select Adjectives:**")
            selected_adjective_custom = {}
            for key, values in adjectives.items():
                selected_adjective_custom[key] = st.selectbox(f"Select {key}:", values, key=f'custom_{key.lower()}')
            custom_selection['adjective'] = selected_adjective_custom

        # Look
        if select_look:
            selected_look_custom = st.selectbox("Select a look:", list(looks.keys()), key='custom_look')
            custom_selection['look'] = selected_look_custom

        # Feel
        if select_feel:
            selected_feel_custom = st.selectbox("Select a feel:", list(feels.keys()), key='custom_feel')
            custom_selection['feel'] = selected_feel_custom

        # Vibe
        if select_vibe:
            selected_vibe_custom = st.selectbox("Select a vibe:", list(vibes.keys()), key='custom_vibe')
            custom_selection['vibe'] = selected_vibe_custom

        submit_custom = st.form_submit_button("Generate Custom Selection")

    if submit_custom:
        # Start building the final selection
        final_selection = {}

        # Category & Type
        if select_category_type:
            final_selection['category'] = custom_selection['category']
            final_selection['type'] = custom_selection['type']
        else:
            category_rand, type_rand, _, _, _, _ = generate_random()
            final_selection['category'] = category_rand
            final_selection['type'] = type_rand

        # Adjectives
        if select_adjectives:
            final_selection['adjective'] = custom_selection['adjective']
        else:
            final_selection['adjective'] = {key: random.choice(values) for key, values in adjectives.items()}

        # Look
        if select_look:
            final_selection['look'] = custom_selection['look']
        else:
            final_selection['look'] = random.choice(list(looks.keys()))

        # Feel
        if select_feel:
            final_selection['feel'] = custom_selection['feel']
        else:
            final_selection['feel'] = random.choice(list(feels.keys()))

        # Vibe
        if select_vibe:
            final_selection['vibe'] = custom_selection['vibe']
        else:
            final_selection['vibe'] = random.choice(list(vibes.keys()))

        # Save to history
        st.session_state.history.append(final_selection)
        st.success("Custom selection generated and saved to history!")

        # Display the custom selection
        st.markdown(f"""
            <div class="card">
                <div class="header">Custom Selection</div>
                <div style="display: flex; gap: 40px;">
                    <div>
                        <div class="subheader">Category & Type</div>
                        <p><strong>Category:</strong> {final_selection['category']}</p>
                        <p><strong>Type:</strong> {final_selection['type']}</p>
                    </div>
                    <div>
                        <div class="subheader">Look & Feel</div>
                        <p><strong>Look:</strong> {final_selection['look']}</p>
                        <p><strong>Feel:</strong> {final_selection['feel']}</p>
                    </div>
                </div>
                <div>
                    <div class="subheader">Adjectives & Vibe</div>
                    <p><strong>Adjectives:</strong></p>
                    <ul>
                        {''.join([f'<li class="list-item">{key}: {value}</li>' for key, value in final_selection['adjective'].items()])}
                    </ul>
                    <p><strong>Vibe:</strong> {final_selection['vibe']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
