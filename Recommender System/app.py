import streamlit as st 
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cac4fda95a3670eefb6faba212757b7e'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
    
similarity = pickle.load(open('C:/DeployML/Recommender System/similarity.pkl','rb'))
movies = pickle.load(open('C:/DeployML/Recommender System/movies.sav','rb'))
movies_list = movies['title'].values

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] # fetching index of each movie
    distances = similarity[movie_index] # calculating distances with all other movies based on cosine similarity
    movielist = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6] # sorting distances array in reverse and fetching top 5 distances
    recommended_movies = []
    recommended_movie_posters = []

    for i in movielist:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movie_posters

st.title('CineAdvisor')

selected_movie = st.selectbox('Search for the movie you want me to recommend for', movies_list)

if st.button('Give me movies'):
    names, posters = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
