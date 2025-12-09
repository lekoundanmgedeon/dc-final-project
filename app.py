import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="CollectToolsBox | DC Final",
    layout="wide",
    page_icon="assets/images.jpeg",
    initial_sidebar_state="expanded"
)




# --- SIDEBAR ---
st.sidebar.title("📌 Menu")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "🕷️ Scraping",
        "📁 Data",
        "⚙️ Settings",
        "❓ About"
    ]
)

# --- IMPORT DES PAGES ---
import modules.home as home
import modules.dashboard as dashboard
import modules.scraping as scraping
import modules.data as data
import modules.settings as settings
import modules.about as about

# --- ROUTING ---
if menu == "🏠 Home":
    home.run()

elif menu == "📊 Dashboard":
    dashboard.run()

elif menu == "🕷️ Scraping":
    scraping.run()

elif menu == "📁 Data":
    data.run()

elif menu == "⚙️ Settings":
    settings.run()

elif menu == "❓ About":
    about.run()


