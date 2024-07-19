import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import nltk
from nltk import PorterStemmer
import csv

with open('stopwords.csv','r') as file:
    reader = csv.reader(file)
    stpwrds = [row[0] for row in reader]
st.title('Word Cloud')

@st.cache_data
def load_dataset():
    with st.spinner("loading ..."):
        return pd.read_csv('scopus.csv')

df = load_dataset()   

ps = PorterStemmer()

tab1, tab2, tab3 = st.tabs(['Word Cloud for Titles', 'Word Cloud for Author Keywords', 'Word Cloud for Index Keywords'])
years = df['Year'].unique()
with tab1:
    year1 = st.selectbox('select the year to chow the most used word in the Titles', options=years, key=1)
    def word_cloud1(data, year):
        titles = data[(data['Year'] == year) & (data['Title'].notna())]['Title']
        text = ''
        for title in titles:
            for word in title.lower().split(' '):
                if word not in stpwrds:
                    text += ' '+ ps.stem(word)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        figure1  = plt.figure(figsize=(50, 30))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'WordCloud for Title in {year}')
        return figure1
    with st.spinner('wait...'):
        figure1 = word_cloud1(df, year1)
        st.pyplot(figure1)

with tab2:
    year3 = st.selectbox('select the year to chow the most used word in the Author Keywords', options=years, key=2)
    def word_cloud3(data, year):
        titles = data[(data['Year'] == year) & (data['Author Keywords'].notna())]['Author Keywords']
        text = ''
        for title in titles:
            for word in title.lower().split(';'):
                if word not in stpwrds:
                    text += ' '+ ps.stem(word)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        figure2 = plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'WordCloud for Author Keywords in{year}')
        return figure2
    with st.spinner('wait...'):
        figure3 = word_cloud3(df, year3)
        st.pyplot(figure3)

with tab3:
    year3 = st.selectbox('select the year to chow the most used word in the Index Keywords', options=years, key=3)
    def word_cloud3(data, year):
        titles = data[(data['Year'] == year) & (data['Index Keywords'].notna())]['Index Keywords']
        text = ''
        for title in titles:
            for word in title.lower().split(';'):
                if word not in stpwrds:
                    text += ' '+ ps.stem(word)
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        figure2 = plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'WordCloud for Index Keywords in{year}')
        return figure2
    with st.spinner('wait...'):
        figure3 = word_cloud3(df, year3)
        st.pyplot(figure3)
