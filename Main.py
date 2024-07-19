import streamlit as st

st.set_page_config(
    page_title="ScopusApp",
    page_icon="〰️"
)

st.title("Welcome to ScopusApp")
st.sidebar.success("HELLO", icon="👋")
st.write("This application gives  some beatifull charts for data visualization")
st.write("It gives also statistics for the scopus dataset,  in order to extract some informations.")
