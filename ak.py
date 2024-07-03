import pickle
import pandas as pd
import streamlit as st

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = similarity[movie_index]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load data from pickle files
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set Streamlit app title and header
st.set_page_config(page_title='Cine Suggest', page_icon=':clapper:', layout='wide')
st.title('Cine Suggest')
st.header('Discover Your Next Favorite Movie!')

# Style adjustments
st.markdown("""
    <style>
    .main {
        background-color: #000000;  /* Black background color */
        color: white;  /* White text color */
        padding: 10px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .css-18e3th9 h1 {
        color: #FF6347;  /* Tomato color for the title */
    }
    .css-18e3th9 h2 {
        color: #4682B4;  /* SteelBlue color for the header */
    }
    </style>
""", unsafe_allow_html=True)

# Dropdown to select a movie
option = st.selectbox(
    'Select a Movie',
    movies['title'].values)

# Button to trigger recommendation
if st.button('Get Recommendations'):
    recommendations = recommend(option)
    st.header('You Might Also Like:')
    for i, movie in enumerate(recommendations, 1):
        st.markdown(f"{i}. **{movie}**")









