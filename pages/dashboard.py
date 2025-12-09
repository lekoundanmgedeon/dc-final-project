import streamlit as st
import pandas as pd
import os
import plotly.express as px
import plotly.figure_factory as ff

# ---------------------------------------
# Charger un fichier spécifique dans /data
# ---------------------------------------
def load_file(filename):
    file_path = os.path.join("data", filename)

    try:
        if filename.endswith(".csv"):
            return pd.read_csv(file_path)
        else:
            return pd.read_excel(file_path)
    except Exception as e:
        st.error(f"Erreur lors du chargement : {e}")
        return None


def run():
    st.title("📊 Dashboard - Visualisation des données")

    # ---------------------------------------
    # 🗂️ Liste des fichiers disponibles
    # ---------------------------------------
    folder = "data"
    if not os.path.exists(folder):
        st.warning("Le dossier /data n'existe pas encore.")
        return

    files = [f for f in os.listdir(folder) if f.endswith((".csv", ".xlsx"))]

    if not files:
        st.warning("Aucun fichier disponible dans /data.")
        return

    st.subheader("📁 Choisir un fichier à visualiser")
    selected_file = st.selectbox("Fichier disponible :", files)

    # Charger le fichier choisi
    df = load_file(selected_file)

    if df is None:
        st.error("Impossible de charger le fichier.")
        return

    st.success(f"📂 Fichier chargé : {selected_file}")
    st.write("Aperçu des données :")
    st.dataframe(df.head())

    st.write("---")
    st.subheader("🎛️ Options de visualisation")

    # ---------------------------------------
    # Préparation des types de colonnes
    # ---------------------------------------
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    viz_type = st.selectbox(
        "Type de graphique",
        ["Histogramme", "Bar Chart", "Pie Chart", "Heatmap de corrélation"]
    )

    # --------------------------------------
    # HISTOGRAMME
    # --------------------------------------
    if viz_type == "Histogramme":
        if not numeric_cols:
            st.error("Aucune colonne numérique disponible.")
        else:
            col = st.selectbox("Choisir une colonne numérique :", numeric_cols)
            fig = px.histogram(df, x=col, nbins=30, title=f"Histogramme de {col}")
            st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------
    # BAR CHART
    # --------------------------------------
    elif viz_type == "Bar Chart":
        if not categorical_cols:
            st.error("Aucune colonne catégorielle disponible.")
        else:
            col = st.selectbox("Choisir une colonne catégorielle :", categorical_cols)

            # Préparation des données
            value_counts = df[col].value_counts().reset_index()
            value_counts.columns = ["category", "count"]  # évite l’erreur Plotly

            # Graphique
            fig = px.bar(
                value_counts,
                x="category",
                y="count",
                title=f"Répartition de {col}"
            )
            st.plotly_chart(fig, use_container_width=True)


    # --------------------------------------
    # PIE CHART
    # --------------------------------------
    elif viz_type == "Pie Chart":
        if not categorical_cols:
            st.error("Aucune colonne catégorielle disponible.")
        else:
            col = st.selectbox("Choisir une colonne catégorielle :", categorical_cols)
            fig = px.pie(df, names=col, title=f"Répartition de {col}")
            st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------
    # HEATMAP
    # --------------------------------------
    elif viz_type == "Heatmap de corrélation":
        if len(numeric_cols) < 2:
            st.error("Besoin d'au moins 2 colonnes numériques pour une heatmap.")
        else:
            corr = df[numeric_cols].corr()
            fig = px.imshow(corr, text_auto=True, title="Heatmap de corrélation")
            st.plotly_chart(fig, use_container_width=True)

