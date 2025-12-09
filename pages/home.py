import streamlit as st

def run():
    st.title(" Welcome to my beautiful CollectToolsBox ! ")
    
    # ---------------------------------------
    # General presentation
    # ---------------------------------------
    st.subheader("🌟 Presentation about the Application")
    st.markdown("""
        This application is a **complete tool for web data processing and analysis**.  
        It allows you to:
        - Scrape data from websites.
        - Import and clean CSV or Excel data.
        - Visualize and analyze your data using an interactive dashboard.
        - Quickly get KPIs and insights.
    """)
    
    st.write("---")
    
    # ---------------------------------------
    # User guide / workflow
    # ---------------------------------------
    st.subheader("📋 Complete User Guide")
    
    st.markdown("""
                1️⃣ **Data Scraping**  
                - Go to the **Scraping** tab.  
                - Enter the website URL and the number of pages to scrape.  
                - The data will be collected and stored automatically.

                2️⃣ **Import and process data**  
                - Go to the **Data** tab.  
                - Upload your raw CSV or Excel files.  
                - View the data and apply **cleaning operations**:  
                - Remove duplicates  
                - Remove missing values  
                - Convert columns to numeric  
                - Standardize column names  
                - Download the cleaned files for further use.

                3️⃣ **Dashboard and visualization**  
                - Go to the **Dashboard** tab.  
                - Select the file you want to visualize from the cleaned data.  
                - Apply **interactive filters**: price, location, categories.  
                - View **KPIs**: total items, average/min/max price, number of locations.  
                - Explore your data through graphs: Histogram, Bar Chart, Pie Chart, Heatmap.
    """)

    st.write("---")
    
    # ---------------------------------------
    # Feedback form
    # ---------------------------------------
    st.subheader("📝 Give us your feedback")
    st.markdown("""
        We value your opinion! Please use one of the following links to give your feedback:

        - [Google Form](https://forms.gle/rXA7wcgMxS3cMaWF8)  
        - [KoboToolbox Form](https://ee.kobotoolbox.org/x/a7BSWphJ)
    """)
    
    st.write("---")
    st.info("Use the top-left menu to navigate through all features.")