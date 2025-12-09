import streamlit as st
import pandas as pd

def run():
    st.title("Data")
    uploaded_file = st.file_uploader("Importer un fichier", type=["csv", "xlsx"])

    if uploaded_file:
        st.success("Fichier importé !")
        try:
            df = pd.read_csv(uploaded_file)
        except:
            df = pd.read_excel(uploaded_file)

        st.dataframe(df)
