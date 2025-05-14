import streamlit as st
from PIL import Image
import numpy as np
import os
import random

# ✅ Updated movie poster paths (match actual .jpg files)
POSTER_DIR = os.path.join(os.path.dirname(__file__), "posters")

movies = {
    "Avatar": os.path.join(POSTER_DIR, "Avatar.jpg"),
    "Tangled": os.path.join(POSTER_DIR, "Tangled.jpg"),
    "Spectre": os.path.join(POSTER_DIR, "Spectre.jpg"),
    "The Avengers": os.path.join(POSTER_DIR, "The_Avengers.jpg"),
    "The Dark Knight Rises": os.path.join(POSTER_DIR, "The_Dark_Knight_Rises.jpg")
}

# ✅ Ensure poster paths are correct

st.title("🎬 Smart Cold-Start Recommender")

# Let user pick a movie
selected_movie = st.selectbox("Pick a Movie", list(movies.keys()))

# Simulate user interactions
hover_time = st.slider("Poster Hover Time (sec)", 0, 30, 10)
trailer_time = st.slider("Trailer Watched (sec)", 0, 120, 60)
interaction_depth = st.slider("Interaction Depth Score", 0.0, 1.0, 0.6)

# Show selected poster
poster_path = movies[selected_movie]
if os.path.exists(poster_path):
    st.image(poster_path, width=250, caption=f"{selected_movie}")
else:
    st.warning(f"⚠️ Poster not found: {poster_path}")

# Generate recommendations (random scores for demo)
@st.cache_data
def recommend(movie, hover, trailer, depth):
    scores = {m: random.uniform(0, 1) for m in movies if m != movie}
    sorted_movies = sorted(scores.items(), key=lambda x: -x[1])
    return sorted_movies[:3]

# Show recommendations
if st.button("Recommend"):
    st.subheader("📌 Top Recommendations Based on Your Interactions:")
    recs = recommend(selected_movie, hover_time, trailer_time, interaction_depth)
    for title, score in recs:
        path = movies[title]
        if os.path.exists(path):
            st.image(path, width=200, caption=f"{title} (score: {score:.2f})")
        else:
            st.markdown(f"❌ {title} (score: {score:.2f}) — Poster missing")