import streamlit as st

def run():
    st.title("❓ About / Documentation")

    st.subheader("🌟 Application Overview")
    st.markdown("""
This application is designed as a **full pipeline for web data extraction, processing, and visualization**.  
It allows users to collect data from websites, clean and preprocess it, and generate interactive dashboards for analysis.

**Primary objectives of the application:**
- Facilitate data scraping from web sources.
- Allow easy import and preprocessing of raw CSV or Excel files.
- Provide interactive visualizations and KPIs to understand the data.
- Support decision-making based on cleaned datasets.
    """)

    st.write("---")

    st.subheader("🛠️ Core Features")

    st.markdown("""
1️⃣ **Web Scraping Module**  
- Users can scrape data from any supported website.  
- Input parameters:  
  - **URL of the target page**  
  - **Number of pages** to scrape  
- The module extracts structured data including titles, prices, locations, images, and links.  
- The resulting dataset can be exported as CSV for further analysis.

2️⃣ **Data Management Module**  
- Allows importing external datasets in **CSV** or **Excel** format.  
- Users can preview the dataset immediately after upload.  
- Supports basic data preprocessing and cleaning:  
  - Remove duplicates  
  - Handle missing values  
  - Convert data types  
  - Standardize column names  
- Cleaned datasets are stored locally in the `/data` folder for further use in the dashboard.

3️⃣ **Dashboard & Visualization Module**  
- Users can select any dataset from the `/data` folder for visualization.  
- Supports interactive filtering by numeric ranges (e.g., price) and categorical values (e.g., location).  
- Displays **Key Performance Indicators (KPIs)** such as:  
  - Total number of items  
  - Average, minimum, and maximum prices  
  - Number of unique locations  
- Supports multiple visualization types:  
  - Histogram (numeric distributions)  
  - Bar Chart (categorical counts)  
  - Pie Chart (category shares)  
  - Heatmap (correlation between numeric variables)  
- Enables a detailed overview of the data for exploratory analysis.

4️⃣ **Workflow / User Guide**  
- **Step 1: Scraping** – collect data from websites and save raw datasets.  
- **Step 2: Data Import & Cleaning** – import external or scraped data, clean, and preprocess.  
- **Step 3: Dashboard** – visualize and explore KPIs and metrics interactively.  
- This structured workflow ensures reproducibility and clarity for data analysis tasks.

5️⃣ **Feedback & Evaluation**  
- Users can provide feedback via external forms such as **Google Forms** or **KoboToolbox**.  
- This allows continuous improvement of the application.

    """)

    st.write("---")

    st.subheader("📌 Use Cases / Applications")
    st.markdown("""
- **Market analysis**: Scrape product listings, analyze prices, and identify trends.  
- **Real estate**: Collect property listings, visualize price distributions and locations.  
- **E-commerce monitoring**: Track competitor products, prices, and availability.  
- **Data science learning**: Practice data cleaning, preprocessing, and visualization on real datasets.  
- **Reporting**: Generate KPIs and charts for presentations or decision-making.
    """)

    st.write("---")

    st.subheader("💡 Tips & Recommendations")
    st.markdown("""
- Always inspect your scraped data for missing or inconsistent values before analysis.  
- Use the dashboard filters to focus on subsets of interest.  
- Regularly clean and update datasets for accurate KPIs.  
- Organize datasets in the `/data` folder with clear file names for easy selection.  
- When scraping multiple websites, keep consistent column naming for easier dashboard visualization.
    """)

    st.write("---")

    st.subheader("🔗 Additional Resources")
    st.markdown("""
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  
- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)  
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    """)

    st.info("Use the sidebar menu to navigate between Scraping, Data, and Dashboard modules for full functionality.")

