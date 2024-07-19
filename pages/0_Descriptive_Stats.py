import pandas as pd
import streamlit as st
import plotly.express as px


@st.cache_data
def load_dataset():
    with st.spinner("loading..."):
        return pd.read_csv('scopus.csv')

df = load_dataset()    
st.title("Welcome to General Stats")


nombre_lignes = st.slider('choisir nombre des lignes a afficher:', min_value=2, max_value=len(df))
colonnes = st.multiselect('selectionner les colonnes a afficher:', options=df.columns.to_list(), default=df.columns,to_list())
st.write(df[:nombre_lignes][colonnes])

n1 = len(df)
n2 = df['Publisher'].nunique()
n3 = df['Sponsors'].nunique()
n4 = df['Editors'].nunique()
n5 = df['Source title'].nunique()
n6 = df['Document Type'].nunique()
n7 = df['Language of Original Document'].nunique()
n8 = df['Affiliations'].nunique()
st.header('DESCRIPTIVE STATS')

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.info('Total number of Documents', icon='✔️')
    st.metric('', value=f"{n1}")
    st.info('Total number of Source', icon='✔️')
    st.metric('', value=f"{n5}")
   
    
with col2:
    st.info('Total number of Publishers', icon='✔️')
    st.metric('', value=f"{n2}")
    st.info('Total number of Document Types', icon='✔️')
    st.metric('', value=f"{n6}")
with col3:
    st.info('Total number of Sponsors', icon='✔️')
    st.metric('', value=f"{n3}")
    st.info('Total number of Languages', icon='✔️')
    st.metric('', value=f"{n7}")
with col4:
    st.info('Total number of Editors', icon='✔️')
    st.metric('', value=f"{n4}")
    st.info('Total number of Affiliations', icon='✔️')
    st.metric('', value=f"{n8}")
