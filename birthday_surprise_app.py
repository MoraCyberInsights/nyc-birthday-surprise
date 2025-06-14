import streamlit as st
from datetime import datetime
from PIL import Image

# --- Customization Settings ---
trip_title = "🗽 Surprise NYC Adventure!"
departure_date = datetime(2025, 6, 21)
days_left = (departure_date - datetime.now()).days

# --- Page Setup ---
st.set_page_config(
    page_title="Birthday Surprise 💝",
    page_icon="🎉",
    layout="centered"
)

# --- Load Media ---
personal_photo = Image.open("images/us_together.jpg")  # Replace with your actual image
header_image = Image.open("images/nyc_skyline.jpg")  # Ensure this image exists in ./images

# --- Initial UI ---
st.image(personal_photo, use_container_width=True)
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Happy Birthday! 🎂</h1>", unsafe_allow_html=True)

if "reveal_trip" not in st.session_state:
    st.session_state.reveal_trip = False

if not st.session_state.reveal_trip:
    if st.button("🎁 Tap twice to Reveal Surprise Destination!"):
        st.session_state.reveal_trip = True
else:
    st.image(header_image, use_container_width=True)
    st.markdown(f"## ✈️ We’re going to **New York City** in **{days_left} days**! 🎉")
    st.markdown("Get ready! I planned a weekend for us. Te amo!")

    # --- Trip Itinerary ---
    st.header("🗽 Trip Itinerary")

    with st.expander("📅 Saturday, June 21"):
        st.markdown("""
        - 🚗 Leave home by **4:00 AM**, park at Park & Ride        
        - ✈️ Flight leaves Austin at **6:00 AM** (arrive at airport by 4:30 AM)
        - 🛬 Arrive at Newark Airport **10:43 AM**
        - 🚕 Transit to Manhattan, arrive around **11:40 AM**
        - 🏨 Early Check-In @ **CitizenM Bowery** – 12:30 PM
        - 📚 Visit **Strand Bookstore** – Pick up "Walking New York" book
        - 🍽️ Dinner Reservation @ **Pastis** – 8:00 PM
        """)

    with st.expander("📅 Sunday, June 22"):
        st.markdown("""
        - 🍳 Breakfast Reservation @ **Lafayette** – 9:30 AM
        - 🛍️ Free time to explore from 11:00 AM to 5:00 PM
        - 🍕 Lunch @ **Ceres Pizza** – 1:00 PM (expect a line!)
        - 🍴 Light dinner or snack before the show
        - 🎭 **Stranger Things: The First Shadow** @ Marquis Theatre – 7:00 PM
        - 🍝 Late Dinner @ **Carbone** – 11:15 PM
        """)

    with st.expander("📅 Monday, June 23"):
        st.markdown("""
        - ☕ Morning coffee adventure
        - 🥯 Breakfast @ **Katz's Deli**
        - 🍷 Dinner Reservation @ **Raoul’s** (French Bistro) – 9:45 PM
        """)

    with st.expander("📅 Tuesday, June 24"):
        st.markdown("""
        - 🥞 Brunch Reservation @ **Friend of a Farmer (Gramercy)** – 10:00 AM
        - ✈️ Leave Manhattan by **5:00 PM** to arrive at airport by 7:00 PM
        - 🛫 Flight to Austin departs **9:00 PM**, arrives **12:00 AM**
        """)

    st.header("📍 Things To Do (Anytime!)")
    with st.expander("🗺️ Our NYC Bucket List"):
        st.markdown("""
        - 🥐 Visit **Supermoon Bakehouse**
        - 🍸 **Double Chicken Please** (80% walk-in bar)
        - 🛍️ Shopping along **5th Ave** and **SoHo**
        - 🌳 Picnic @ **Central Park**
        - 🖼️ Visit the **MET**
        - 🥟 Explore **Chinatown Dumpling Tour**:
            - North Dumpling
            - King Dumpling
        - ☕ Coffee from **787 Coffee** (East Village)
        - 🍪 **Culture Espresso** (amazing cookies)
        - 🔐 Speakeasy @ **Please Don’t Tell**
        - ⛴️ **Ferry from Wall St. to DUMBO**, then walk across Brooklyn Bridge
        - 🏃‍♂️ Morning run in Central Park
        - 🍰 Dessert from **William Greenberg Desserts**
        - 🍦 Little treat from **Dudleys NYC** (truffle fries and soft serve)
        - 🍕 Highly rated pizza from **John's of Bleecker Street**
        - 🗽 Many others I have saved on my phone
        """)

    # --- Slideshow Section ---
    st.header("🖼️ NYC Moodboard")

    image_paths = [
        "images/Stranger Things.jpg",
        "images/Carbone.webp",
        "images/CeresPizza.jpg",
        "images/Katz.jpg",
        "images/Lafayette.jpg",
        "images/CitizenM.jpg",
        "images/Pastis.webp",
    ]

    captions = [
        "Stranger Things",
        "Carbone",
        "Ceres Pizza",
        "Katz's Delicatessen",
        "Larfayette",
        "CitizenM Bowery Hotel",
        "Pastis"
    ]

    if "slide_index" not in st.session_state:
        st.session_state.slide_index = 0

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        if st.button("⬅️"):
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(image_paths)

    with col3:
        if st.button("➡️"):
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(image_paths)

    img = Image.open(image_paths[st.session_state.slide_index])
    st.image(img, use_container_width=True, caption=captions[st.session_state.slide_index])

    
    st.markdown("---")
    st.markdown("### 💌 Una aventura para el amor de mi vida. I can't wait to experience this with you. Thank you for being my everything. ❤️")

    # --- Footer ---
    st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with 💖 by your husband</p>", unsafe_allow_html=True)
