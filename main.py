import streamlit as st
import random

# Expanded Dictionaries for the categories
types = {
    "Wall Decor": [
        "Painting", "Tapestry", "Mirror", "Wall Clock", "Wall Sticker", "Wall Shelf",
        "Photo Frame", "Mirrored Art", "Shadow Box", "Wall Paneling", "Canvas Print",
        "Metal Wall Art", "3D Wall Sculpture", "Wooden Wall Art", "Fabric Wall Art",
        "LED Wall Light", "Decorative Wall Hooks", "Vinyl Wall Decals", "Framed Posters",
        "Decorative Wall Tiles", "Macramé Wall Hanging"
    ],
    "Table Decor": [
        "Vase", "Candle Holder", "Ornament", "Bookend", "Tray", "Table Lamp",
        "Centerpiece", "Fruit Bowl", "Decorative Plates", "Coasters", "Salt and Pepper Shakers",
        "Napkin Holder", "Decorative Tray", "Table Runner", "Candle Lantern", "Desk Organizer",
        "Decorative Bowls", "Succulent Holders", "Miniature Figurines", "Table Clock",
        "Decorative Books", "Tabletop Fountain", "Terrarium", "Decorative Wine Rack"
    ],
    "Lighting": [
        "Lamp", "Lantern", "Chandelier", "String Lights", "Sconce", "Desk Lamp",
        "Floor Lamp", "Pendant Light", "Wall Sconce", "LED Strip Lights", "Desk Light",
        "Hanging Lantern", "Task Lighting", "Smart Bulb", "Neon Light Sign",
        "Solar Light", "Fiber Optic Lamp", "Paper Lanterns", "Geometric Light Fixtures",
        "Vintage Edison Bulb Fixtures"
    ],
    "Soft Decor": [
        "Throw Pillow", "Blanket", "Rug", "Curtain", "Bean Bag", "Decorative Cushion",
        "Faux Fur Throw", "Ottoman", "Window Liner", "Seat Cushion", "Decorative Pouf",
        "Floor Cushion", "Bedspread", "Decorative Curtains", "Lounge Pillow", "Quilt",
        "Tapestry", "Fabric Wall Art", "Decorative Bed Pillows", "Sheer Curtains",
        "Patterned Throw Blankets", "Velvet Cushions", "Woven Poufs", "Decorative Throws"
    ],
    "Functional Decor": [
        "Planter", "Key Holder", "Coat Rack", "Jewelry Box", "Wall-mounted Planter",
        "Mail Organizer", "Umbrella Stand", "Magazine Rack", "Jewelry Stand", "Wall Hooks",
        "Shoe Rack", "Key Organizer", "Coat Hanger", "Storage Basket",
        "Decorative Storage", "Wall-mounted Shelves", "Tool Organizer", "Cable Management Station",
        "Decorative Baskets", "Entryway Organizer", "Multi-functional Furniture",
        "Decorative Hooks", "Bike Rack", "Wall-mounted Drying Rack"
    ],
    "Art Pieces": [
        "Sculpture", "Figurine", "Abstract Art", "Statue", "Relief Art", "Wall Sculpture",
        "Canvas Art", "Metal Art", "Glass Art", "Wooden Art", "Mosaic Art",
        "Mixed Media Art", "Digital Art", "Kinetic Sculpture", "Ceramic Art",
        "Paper Art", "Stone Carving", "Brass Art", "Recycled Art", "Light Art",
        "Wire Art", "Clay Art", "Enamel Art", "Textile Art"
    ],
    "Seasonal Decor": [
        "Christmas Tree", "Pumpkin", "Wreath", "Garland", "Halloween Pumpkin",
        "Easter Egg Display", "Thanksgiving Centerpiece", "Hanukkah Menorah",
        "Valentine's Heart Decor", "Spring Bouquet", "Summer Garland",
        "Autumn Leaves Decor", "Winter Icicles", "Festive Lights",
        "Seasonal Figurines", "Holiday Candles", "Seasonal Tablecloth",
        "Seasonal Banners", "Holiday Ornaments", "Seasonal Pillows",
        "New Year Decor", "Diwali Lanterns", "Ramadan Decorations",
        "St. Patrick's Day Decor", "Fourth of July Flags"
    ],
    "Other": [
        "Room Divider", "Decorative Basket", "Accent Furniture", "Clock",
        "Decorative Screen", "Storage Basket", "Accent Chair", "Console Table",
        "Decorative Tray", "Pet Bed", "Decorative Clock", "Folding Screen",
        "Decorative Lantern", "Decorative Mirror", "Bookcase", "Side Table",
        "Bar Cart", "Decorative Planter", "Indoor Fountain", "Decorative Vase",
        "Scented Candle Holder", "Decorative Storage Ottoman",
        "Entryway Bench", "Decorative Pouf", "Accent Table"
    ]
}

adjectives = {
    "Size": ["Tiny", "Small", "Medium", "Large", "Oversized", "Petite", "Compact", "Generous", "Grand", "Miniature"],
    "Shape": ["Round", "Square", "Rectangular", "Triangular", "Irregular", "Oval", "Hexagonal", "Circular", "Oblong", "Asymmetrical"],
    "Material": ["Wooden", "Metallic", "Ceramic", "Glass", "Woven", "Plastic", "Stone", "Fabric", "Leather", "Paper",
                "Concrete", "Marble", "Bamboo", "Resin", "Brass", "Copper", "Iron", "Silk", "Velvet", "Lacquer"],
    "Color": ["Vibrant", "Pastel", "Neutral", "Monochrome", "Gradient", "Bold", "Earth-toned", "Bright", "Dark", "Light",
              "Muted", "Multicolored", "Primary-colored", "Secondary-colored", "Primary Palette", "Warm-toned",
              "Cool-toned", "Jewel-toned", "Metallic-colored", "Primary Colors"],
    "Finish": ["Glossy", "Matte", "Polished", "Textured", "Aged", "Distressed", "Brushed", "Shimmering", "Satin",
               "Matte", "Lacquered", "Patinated", "Antiqued", "Hammered", "Rustic", "Smooth", "Rough", "Satin-finished",
               "Embossed", "Engraved"],
    "Decorative Detail": ["Patterned", "Plain", "Engraved", "Painted", "Studded", "Embellished", "Beaded", "Printed",
                          "Laser-cut", "Hand-painted", "Intricate", "Ornate", "Geometric", "Floral", "Abstract",
                          "Striped", "Polka-dotted", "Chevron", "Paisley", "Camouflage"],
    "Theme Specific": ["Geometric", "Floral", "Abstract", "Nature-Inspired", "Minimalist", "Vintage", "Rustic",
                        "Modern", "Art Deco", "Scandinavian", "Bohemian", "Industrial", "Eclectic", "Mid-Century",
                        "Contemporary", "Traditional", "Farmhouse", "Nautical", "Tropical", "Zen"]
}

looks = {
    "Modern": ["Sleek", "Minimalist", "Clean Lines", "Contemporary", "Futuristic"],
    "Traditional": ["Ornate", "Detailed", "Classic", "Elegant", "Timeless"],
    "Rustic": ["Raw", "Weathered", "Earthy", "Handcrafted", "Natural"],
    "Industrial": ["Metallic", "Rough", "Functional", "Exposed", "Urban"],
    "Vintage": ["Antique", "Faded", "Nostalgic", "Retro", "Timeless"],
    "Eclectic": ["Mixed", "Bohemian", "Vibrant", "Colorful", "Diverse"],
    "Luxurious": ["Opulent", "Rich", "Elegant", "Sumptuous", "Grand"],
    "Artistic": ["Creative", "Unique", "Expressive", "Avant-garde", "Innovative"],
    "Scandinavian": ["Simple", "Functional", "Light", "Minimalist", "Cozy"],
    "Mid-Century": ["Retro", "Geometric", "Bold Colors", "Organic Shapes", "Minimalist"],
    "Farmhouse": ["Shabby Chic", "Rustic", "Cozy", "Vintage", "Homely"],
    "Nautical": ["Marine", "Sea-inspired", "Blue-toned", "Sailor-themed", "Beachy"],
    "Tropical": ["Vibrant", "Lush", "Leafy", "Bright", "Exotic"],
    "Zen": ["Calm", "Balanced", "Harmonious", "Peaceful", "Minimalist"]
}

feels = {
    "Warm": ["Inviting", "Cozy", "Homely", "Comfortable", "Snug"],
    "Cool": ["Refreshing", "Calm", "Serene", "Relaxing", "Tranquil"],
    "Dynamic": ["Energetic", "Bold", "Vivid", "Vibrant", "Lively"],
    "Relaxing": ["Soothing", "Tranquil", "Peaceful", "Calm", "Restful"],
    "Inspiring": ["Uplifting", "Motivating", "Visionary", "Encouraging", "Empowering"],
    "Playful": ["Fun", "Whimsical", "Quirky", "Lighthearted", "Cheerful"],
    "Sophisticated": ["Refined", "Elegant", "Graceful", "Chic", "Polished"],
    "Bohemian": ["Free-Spirited", "Eclectic", "Colorful", "Artistic", "Laid-back"],
    "Cozy": ["Comfortable", "Snug", "Welcoming", "Intimate", "Warm"],
    "Minimalist": ["Clean", "Uncluttered", "Simple", "Essential", "Streamlined"],
    "Elegant": ["Graceful", "Stylish", "Tasteful", "Polished", "Refined"],
    "Modern": ["Sleek", "Stylish", "Contemporary", "Chic", "Trendy"],
    "Rustic": ["Earthy", "Natural", "Handcrafted", "Raw", "Weathered"],
    "Vintage": ["Timeless", "Classic", "Nostalgic", "Retro", "Antique"]
}

vibes = {
    "Coastal": ["Beachy", "Light", "Airy", "Sea-inspired", "Sunny"],
    "Bohemian": ["Layered", "Colorful", "Free-Spirited", "Eclectic", "Artistic"],
    "Urban": ["Contemporary", "Edgy", "Chic", "Modern", "Industrial"],
    "Nature": ["Organic", "Earthy", "Green", "Botanical", "Natural"],
    "Romantic": ["Soft", "Dreamy", "Elegant", "Lush", "Whimsical"],
    "Adventurous": ["Bold", "Dramatic", "Exploratory", "Exciting", "Dynamic"],
    "Festive": ["Bright", "Joyful", "Celebratory", "Colorful", "Lively"],
    "Zen": ["Calm", "Balanced", "Harmonious", "Peaceful", "Tranquil"],
    "Vintage": ["Retro", "Nostalgic", "Timeless", "Classic", "Antique"],
    "Industrial": ["Metallic", "Rough", "Functional", "Exposed", "Urban"],
    "Tropical": ["Vibrant", "Lush", "Exotic", "Bright", "Colorful"],
    "Rustic": ["Earthy", "Natural", "Handcrafted", "Raw", "Weathered"],
    "Minimalist": ["Clean", "Uncluttered", "Simple", "Essential", "Streamlined"],
    "Farmhouse": ["Shabby Chic", "Rustic", "Cozy", "Vintage", "Homely"],
    "Scandinavian": ["Simple", "Functional", "Light", "Minimalist", "Cozy"]
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
st.write("Generate decorative house item designs by selecting categories manually, randomly, or customizing!")

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
method = st.radio("Choose a selection method:", ["Manual", "Random", "Custom Random"], horizontal=True)

if method == "Manual":
    with st.form(key='manual_selection'):
        selected_category = st.selectbox("Select a category:", list(types.keys()))
        selected_type = st.selectbox("Select a type:", types[selected_category])
        st.markdown("**Select Adjectives:**")
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

elif method == "Custom Random":
    st.subheader("Custom Random Selection")
    with st.form(key='custom_random_selection'):
        st.write("Toggle the attributes you want to customize. Unselected attributes will be randomized.")

        # Toggle buttons for each attribute group
        customize_category_type = st.checkbox("Customize Category & Type")
        customize_adjectives = st.checkbox("Customize Adjectives")
        customize_look = st.checkbox("Customize Look")
        customize_feel = st.checkbox("Customize Feel")
        customize_vibe = st.checkbox("Customize Vibe")

        # Initialize a dictionary to hold user inputs
        user_selection = {}

        # Customize Category & Type
        if customize_category_type:
            selected_category_custom = st.selectbox("Select a category:", list(types.keys()), key='custom_category_random')
            selected_type_custom = st.selectbox("Select a type:", types[selected_category_custom], key='custom_type_random')
            user_selection['category'] = selected_category_custom
            user_selection['type'] = selected_type_custom

        # Customize Adjectives
        if customize_adjectives:
            st.markdown("**Customize Adjectives:**")
            selected_adjective_custom = {}
            for key, values in adjectives.items():
                selected_adjective_custom[key] = st.selectbox(f"Select {key}:", values, key=f'custom_random_{key.lower()}')
            user_selection['adjective'] = selected_adjective_custom

        # Customize Look
        if customize_look:
            selected_look_custom = st.selectbox("Select a look:", list(looks.keys()), key='custom_look_random')
            user_selection['look'] = selected_look_custom

        # Customize Feel
        if customize_feel:
            selected_feel_custom = st.selectbox("Select a feel:", list(feels.keys()), key='custom_feel_random')
            user_selection['feel'] = selected_feel_custom

        # Customize Vibe
        if customize_vibe:
            selected_vibe_custom = st.selectbox("Select a vibe:", list(vibes.keys()), key='custom_vibe_random')
            user_selection['vibe'] = selected_vibe_custom

        submit_custom_random = st.form_submit_button("Generate Custom Random Selection")

    if submit_custom_random:
        final_selection = {}

        # Category & Type
        if customize_category_type:
            final_selection['category'] = user_selection['category']
            final_selection['type'] = user_selection['type']
        else:
            category_rand, type_rand, _, _, _, _ = generate_random()
            final_selection['category'] = category_rand
            final_selection['type'] = type_rand

        # Adjectives
        if customize_adjectives:
            final_selection['adjective'] = user_selection['adjective']
        else:
            final_selection['adjective'] = {key: random.choice(values) for key, values in adjectives.items()}

        # Look
        if customize_look:
            final_selection['look'] = user_selection['look']
        else:
            final_selection['look'] = random.choice(list(looks.keys()))

        # Feel
        if customize_feel:
            final_selection['feel'] = user_selection['feel']
        else:
            final_selection['feel'] = random.choice(list(feels.keys()))

        # Vibe
        if customize_vibe:
            final_selection['vibe'] = user_selection['vibe']
        else:
            final_selection['vibe'] = random.choice(list(vibes.keys()))

        # Save to history
        st.session_state.history.append(final_selection)
        st.success("Custom random selection generated and saved to history!")

        # Display the custom random selection
        st.markdown(f"""
            <div class="card">
                <div class="header">Custom Random Selection</div>
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
