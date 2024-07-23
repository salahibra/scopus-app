import streamlit as st
import plotly.express as px
import pandas as pd

@st.cache_data
def load_dataset():
    with st.spinner("loading ..."):
        return pd.read_csv('scopus.csv')

df = load_dataset()   

st.header('The top-50 Source')
editors = df['Source title'].value_counts().reset_index()


tab1, tab2, tab3 = st.tabs(['Document Type', 'Open Access', ' Language of Original Document'])


with tab1:
    source1 = st.selectbox('choose the Source :', options=editors.head(50)['Source title'].to_list(), key=1)
    data1 = df[df['Source title']==source1]['Document Type'].value_counts().reset_index()
    with st.spinner('loading...'):
        st.write('number of publications of the Source ', source1, 'is : ', data1['count'].sum())
        fig_pie1 = px.pie(data1, names='Document Type', values='count', hole=0.3,
                        title='pourcentage of each type of documents')
        st.plotly_chart(fig_pie1)

with tab2:
    source2 = st.selectbox('choose the Source :', options=editors.head(50)['Source title'].to_list(), key=2)
    data2 = df[df['Source title']==source2]['Open Access'].value_counts().reset_index()
    with st.spinner('loading...'):
        st.write('number of publications of the Source: ', source2, 'is : ', data2['count'].sum())
        fig_pie2 = px.pie(data2, names='Open Access', values='count', hole = 0.3, 
                        title='pourcentage of each Open Access Type', )
        st.plotly_chart(fig_pie2)

with tab3:
    source3 = st.selectbox('choose the Source :', options=editors.head(50)['Source title'].to_list(), key=3)
    data3 = df[df['Source title']==source3]['Language of Original Document'].value_counts().reset_index()
    with st.spinner('loading...'):
        st.write('number of publications of the Source: ', source3, 'is : ', data3['count'].sum())
        fig_pie3 = px.pie(data3, names='Language of Original Document', values='count', hole = 0.3, 
                        title='pourcentage of each Language', )
        st.plotly_chart(fig_pie3)



