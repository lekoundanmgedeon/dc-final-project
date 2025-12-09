import streamlit as st

def run():
    st.title("Scraping")
    url = st.text_input("Entrez l’URL à scraper :")

    if st.button("Lancer le scraping"):
        if url:
            st.success(f"Scraping lancé pour : {url}")
        else:
            st.error("Veuillez entrer une URL valide.")
