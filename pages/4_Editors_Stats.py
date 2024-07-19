import streamlit as st
import plotly.express as px
import pandas as pd

@st.cache_data
def load_dataset():
    with st.spinner("loading ..."):
        return pd.read_csv('scopus.csv')

df = load_dataset()   

st.header('The top-50 Editors')
editors = df['Editors'].value_counts().reset_index()


tab1, tab2, tab3 = st.tabs(['Document Type', 'Open Access', ' Language of Original Document'])


with tab1:
    editors1 = st.selectbox('choose the Editors :', options=editors.head(50)['Editors'].to_list(), key=1)
    data1 = df[df['Editors']==editors1]['Document Type'].value_counts().reset_index()
    with st.spinner('loading...'):
        st.write('number of publications of the Editors ', editors1.replace(';', ' and '), 'is : ', data1['count'].sum())
        fig_pie1 = px.pie(data1, names='Document Type', values='count', hole=0.3,
                        title='pourcentage of each type of documents')
        st.plotly_chart(fig_pie1)

with tab2:
    editors2 = st.selectbox('choose the Editors :', options=editors.head(50)['Editors'].to_list(), key=2)
    data2 = df[df['Editors']==editors2]['Open Access'].value_counts().reset_index()
    with st.spinner('loading...'):
        st.write('number of publications of the Editors: ', editors2.replace(';', ' and '), 'is : ', data2['count'].sum())
        fig_pie2 = px.pie(data2, names='Open Access', values='count', hole = 0.3, 
                        title='pourcentage of each Open Access Type', )
        st.plotly_chart(fig_pie2)

with tab3:
    editors3 = st.selectbox('choose the Editors :', options=editors.head(50)['Editors'].to_list(), key=3)
    data3 = df[df['Editors']==editors3]['Language of Original Document'].value_counts().reset_index()
    with st.spinner('loading...'):
        st.write('number of publications of the Editors: ', editors3.replace(';', ' and '), 'is : ', data3['count'].sum())
        fig_pie3 = px.pie(data3, names='Language of Original Document', values='count', hole = 0.3, 
                        title='pourcentage of each Language', )
        st.plotly_chart(fig_pie3)



