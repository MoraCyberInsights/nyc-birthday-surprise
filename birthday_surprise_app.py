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
header_image = Image.open("images/nyc_skyline.jpg")  # Ensure this image exists in ./images
# music_file = "audio/birthday_theme.mp3"  # Optional: Background music

# --- Display Header ---
st.image(header_image, use_container_width=True)
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>We are going to NYC! Happy Birthday! 🎂💕</h1>", unsafe_allow_html=True)

# --- Countdown ---
st.markdown(f"## ✈️ Our adventure begins in **{days_left} days**!")
st.markdown("Get ready for the magic of New York City...")

# --- Reveal Itinerary ---
# Track if the surprise has been revealed
if "revealed" not in st.session_state:
    st.session_state.revealed = False

if st.button("🎁 Tap to Reveal NYC Schedule!"):
    st.session_state.revealed = True

if st.session_state.revealed:

    st.success(trip_title)

    st.header("🗽 Trip Itinerary: June 21–24")

    with st.expander("📅 Saturday, June 21"):
        st.markdown("""
        - ✈️ Flight leaves Austin at **6:00 AM** (arrive at airport by 4:30 AM)
        - 🚗 Leave home by **4:00 AM**, park at Park & Ride
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
        """)

    # --- Slideshow Section ---
    st.header("🖼️ NYC Moodboard")

    image_paths = [
        "images/Stranger Things.jpg",
        "images/CitizenM.jpg",
        "images/CeresPizza.jpg",
        "images/Katz.jpg",
        "images/Lafayette.jpg",
        "images/Carbone.webp",
        "images/Pastis.webp",
    ]

    captions = [
        "Stranger Things",
        "CitizenM Bowery Hotel",
        "Ceres Pizza",
        "Katz's Delicatessen",
        "Lafayette",
        "Carbone",
        "Pastis"
    ]

    # Use session state to track the current image index
    if "slide_index" not in st.session_state:
        st.session_state.slide_index = 0

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        if st.button("⬅️"):
            st.session_state.slide_index = (st.session_state.slide_index - 1) % len(image_paths)

    with col3:
        if st.button("➡️"):
            st.session_state.slide_index = (st.session_state.slide_index + 1) % len(image_paths)

    # Display the current image
    img = Image.open(image_paths[st.session_state.slide_index])
    st.image(img, use_container_width=True, caption=captions[st.session_state.slide_index])

    st.markdown("---")
    st.markdown("### 💌 Una aventura para el amor de mi vida. I can't wait to experience this with you. Thank you for being my everything. ❤️")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with 💖 by your husband</p>", unsafe_allow_html=True)
