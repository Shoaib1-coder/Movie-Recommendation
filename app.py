import streamlit as st
import pandas as pd

# Load the clustered movie dataset
df = pd.read_csv('preprocess.csv') 

st.title("🎬 Movie Recommendation App")
st.markdown("Find movies similar to your favorite  ")

# Dropdown to select a movie
movie_list = sorted(df['title'].unique())
selected_movie = st.selectbox("🎥 Select a Movie:", movie_list)

# Recommend button
if st.button("🔍 Recommend"):
    cluster_label = df[df['title'] == selected_movie]['cluster'].values[0]
    recommendations = df[(df['cluster'] == cluster_label) & (df['title'] != selected_movie)]
    
    st.subheader("📽️ Recommended Movies:")
    if recommendations.empty:
        st.info("No recommendations found in this cluster.")
    else:
        for title in recommendations['title'].sample(n=min(5, len(recommendations))).values:
            st.write(f"✅ {title}")
