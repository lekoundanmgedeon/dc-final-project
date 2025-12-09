import streamlit as st
import pandas as pd
from scraping.scraping_fonction import scrape_pages

def run():
    st.title("🕷️ Scraping")

    st.write("Scrape automatiquement un site selon une URL et un nombre de pages.")

    # INPUTS UTILISATEUR 
    base_url = st.text_input(
        "URL de base (exemple : https://sn.coinafrique.com/categorie/chiens)",
        value="https://sn.coinafrique.com/categorie/chiens"
    )

    total_pages = st.number_input(
        "Nomber de pages à scraper",
        min_value=1,
        max_value=50,
        value=2
    )

    #  BOUTON DE SCRAPING 
    if st.button("Lancer le scraping"):
        if not base_url.strip():
            st.error("Veuillez entrer une URL valide.")
        else:
            with st.spinner("Scraping en cours..."):
                df = scrape_pages(base_url, total_pages)

            st.success("Scraping terminé !")
            st.write(f"Nombre d'annonces trouvées : **{len(df)}**")

            st.dataframe(df)

            # Téléchargement CSV
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Télécharger le CSV",
                csv,
                "scraped_data.csv",
                "text/csv"
            )
