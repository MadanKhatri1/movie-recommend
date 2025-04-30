import streamlit as st
import pandas as pd
import pickle

# Load the similarity matrix
with open('similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

# Load the movie DataFrame (assuming new_df is available as a pickle or CSV)
# Adjust this based on how you store new_df
new_df = pd.read_pickle('movie.pkl')  # or pd.read_csv('movies.csv')

def recommend(movie):
    movie = movie.lower()
    try:
        mov_ind = new_df[new_df['title'] == movie].index[0]
        distances = similarity[mov_ind]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = [new_df.iloc[i[0]].title for i in movie_list]
        return recommended_movies
    except IndexError:
        return ["Movie not found in the database."]

# Streamlit app
st.title("Movie Recommender System")
st.write("Select a movie to get recommendations!")

# Dropdown for movie selection
movie_list = new_df['title'].str.title().tolist()  # Capitalize titles for display
selected_movie = st.selectbox("Choose a movie:", [""] + movie_list)

if selected_movie:
    recommendations = recommend(selected_movie.lower())
    st.subheader("Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")
else:
    st.write("Please select a movie to see recommendations.")