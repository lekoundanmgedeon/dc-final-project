import streamlit as st
import pandas as pd
import os

def save_uploaded_file(uploaded_file):
    folder = "data"
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def run():
    st.title("📁 Data - Import & Preprocessing")

    uploaded_file = st.file_uploader(
        "Importer un fichier (CSV ou Excel)",
        type=["csv", "xlsx"]
    )

    if uploaded_file:

        # --- SAVES ---
        file_path = save_uploaded_file(uploaded_file)
        st.success(f"Fichier enregistré dans : `{file_path}`")

        # --- LOADING---
        try:
            df = pd.read_csv(file_path)
        except:
            df = pd.read_excel(file_path)

        st.subheader("Data overview ")
        st.dataframe(df)

        st.write("---")
        st.subheader("⚙️ Data preprocessing")

        # --- CLEANING OPTIONS ---
        if st.checkbox("Delete all duplicated rows"):
            df = df.drop_duplicates()
            st.success("duplicated remove.!")

        if st.checkbox("Delete rows with missing values"):
            df = df.dropna()
            st.success("rows has missing values deleted.! ")

        if st.checkbox("Convert to numerical column"):
            for col in df.columns:
                try:
                    df[col] = pd.to_numeric(df[col])
                except:
                    pass
            st.success("Conversion has done !.")

        if st.checkbox("Put column name in minuscule"):
            df.columns = [c.lower() for c in df.columns]
            st.success("Colonnes name has changed in minuscule.")

        st.write("---")
        st.subheader("Data preprocessed")
        st.dataframe(df)

        # --- Downloading csv cleaned
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download cleaned csv",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )
