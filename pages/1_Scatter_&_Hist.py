import pandas as pd
import streamlit as st
import plotly.express as px


@st.cache_data
def load_dataset():
    with st.spinner("loading..."):
        return pd.read_csv('scopus.csv')

df = load_dataset()    

st.header('PLOTTING')
colonnes = df.columns.to_list()
colonnes.reverse()
tab1, tab2 = st.tabs(['Scatter Plot', 'Histogram'])
with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        x_col = st.selectbox('choisir la caracteristique sur axe x:', colonnes)
    with col2:
        y_col = st.selectbox('choisir la caracteristique sur axe y:', colonnes)
    with col3:
        color = st.selectbox('choisir la caracteristique color:', colonnes)
    fig_scatter = px.scatter(df, x_col, y_col, color=color)
    st.plotly_chart(fig_scatter)

with tab2:
    feat = st.selectbox('choisir la caracteristique:', colonnes)
    fig_hist = px.histogram(df, x=feat, title='                                    distribution of '+feat)
    fig_hist.update_layout(bargap=0.2)
    fig_hist.update_xaxes(tickvals=df[feat])
    st.plotly_chart(fig_hist)


