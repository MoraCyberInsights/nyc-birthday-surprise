import streamlit as st
from datetime import datetime
from PIL import Image

# --- Customization Settings ---
trip_title = "🗽 Surprise NYC Adventure!"
departure_date = datetime(2025, 6, 21)
days_left = (departure_date - datetime.now()).days

itinerary = [
    "🛫 Flight to NYC – Pack your bags!",
    "🏨 Check-in at hotel – Lower East Side",
    "🗽 Visit the Statue of Liberty – A true American icon.",
    "🎭 Broadway Show: Stranger Things – Orchestra seats, baby!",
    "🌇 Food - Carbone, Pastis, Lafayette",
    "🖼️ Explore The Met Museum – Art, culture, and history.",
    "🛍️ Shopping in SoHo – Fashion capital vibes.",
    "🍎 Picnic in Central Park – Romantic and relaxing.",
    "🛫 Return Home – With memories of a lifetime 💕"
]

# --- Page Setup ---
st.set_page_config(
    page_title="Birthday Surprise 💝",
    page_icon="🎉",
    layout="centered"
)

# --- Load Media ---
header_image = Image.open("images/nyc_skyline.jpg")  # You must place your image in ./images
#music_file = "audio/birthday_theme.mp3"  # Place your music file in ./audio

# --- Display Header ---
st.image(header_image, use_container_width=True)
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Happy Birthday, mi amor! 🎂💕</h1>", unsafe_allow_html=True)

# --- Play Background Music ---
#with open(music_file, "rb") as f:
    #audio_bytes = f.read()
    #st.audio(audio_bytes, format="audio/mp3")

# --- Countdown ---
st.markdown(f"## ✈️ Our adventure begins in **{days_left} days**!")
st.markdown("Get ready for the magic of New York City...")

# --- Reveal Itinerary ---
if st.button("🎁 Tap to Reveal NYC Schedule!"):
    st.success(trip_title)
    for item in itinerary:
        st.markdown(f"- {item}")
    st.markdown("---")
    st.markdown("### 💌 Una aventura para el amor de mi vida. I can't wait to experience this with you. Thank you for being my everything. ❤️")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with 💖 by your husband</p>", unsafe_allow_html=True)
