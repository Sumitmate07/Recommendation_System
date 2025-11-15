import pickle
import pandas as pd
import streamlit as st

#Load the Dataset 


data=pickle.load(open('movies_dict.pkl',mode='rb'))
data=pd.DataFrame(data)
#print(movies)

similarity = pickle.load(open('similarity.pkl',mode='rb'))
print(similarity)


def recommend (movie):

    recommended_movies=[]

    movie_index=data[data['title']==movie].index[0]
    distance =similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]].title)

    return recommended_movies



# Streamlit Web-App
st.title(' Movie Recommendation System :pushpin:')
selected_movie = st.selectbox('Choose your movie:', data['title'].values)
btn=st.button('Recommend')

if btn:
    top_5_movies=recommend(selected_movie)
    for i in top_5_movies:
        st.write(i)





