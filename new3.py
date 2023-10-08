import streamlit as st
import openai
import pandas as pd
import time
import plotly.express as px

# Set the OpenAI API Key (Replace 'XXXXXXXXXXXXX' with your actual API key)
openai.api_key = 'XXXXXXXXXXXXX'

# Create a Streamlit app with improved design
st.set_page_config(page_title="Atlas Analytica", layout="wide")

# Custom CSS to style the app
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        padding: 15px 30px;  # Larger button
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .top-banner {
        background-color: #4CAF50;
        padding: 20px;
        text-align: center;
    }
    .banner-title {
        color: white;
        font-size: 28px;
    }
    .banner-description {
        color: white;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Business Idea Generator
def get_business_idea(country, countryOfResidence):
    with st.spinner("AI is thinking..."):
        time.sleep(3)

    prompt = f"Generate a business idea for people from {country} living in {countryOfResidence}, please provide three examples as to why they are great business ideas."
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )

    idea = response.choices[0].text.strip()
    return idea

# Load the dataset
file_path = 'Datasets/Permanent Resident - Country of Citizenship.xlsx'
df = pd.read_excel(file_path)

# Clean the data
df = df.dropna().reset_index(drop=True)
df = df[['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 4']]
df.columns = ['Country', 'Percentage', 'Base Count']
df = df.iloc[1:]
df['Percentage'] = pd.to_numeric(df['Percentage'], errors='coerce')

# Exclude the total count row and get the specific country with the max percentage
specific_country_df = df.iloc[1:]
specific_country_max_percentage = specific_country_df.loc[specific_country_df['Percentage'].idxmax()]

# Top Banner
st.markdown(
    """
    <div class="top-banner">
        <h1 class="banner-title">Atlas Analytica</h1>
        <p class="banner-description">
        Empowering Entrepreneurs with AI and Data Analytics
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Business Idea Generator Section
st.title("AI-Powered Business Idea Generator")
st.write("Welcome to the AI-powered Business Idea Generator. Our AI model has analyzed data from various countries and industries to provide you with unique business ideas.")
st.write("Simply select a country, and we'll use the power of AI to suggest business ideas tailored to people from that country living in your chosen location.")

# Sidebar for user input
st.sidebar.header("Select Options")
country = st.sidebar.selectbox("Select Country", df['Country'])
countryOfResidence = st.sidebar.text_input("Enter Country of Residence", "Canada")

# Main content area for Business Idea Generator
st.write("Country with max percentage:", specific_country_max_percentage['Country'])
st.write("Percentage:", specific_country_max_percentage['Percentage'])
st.write("Base Count:", specific_country_max_percentage['Base Count'])

# Button to generate the business idea
if st.button("Generate Business Idea", key="business_idea_button"):
    idea = get_business_idea(country, countryOfResidence)
    st.write("Business idea for people from", country, "living in", countryOfResidence, ":")
    st.write(idea)

# Data Visualization Section
st.title("Data Visualizations")
st.write("Explore intriguing visualizations of permanent and temporary residents' data in vibrant colors and engaging charts.")
st.write("Use the following buttons to navigate the data visualizations:")

# DataViz
PRc = pd.read_excel("Datasets/2Permanent_Resident_-_Country_of_Citizenship copy.xlsx")
PRr = pd.read_excel("Datasets/2Permanent_Resident_-_Region_of_Citizenship.xlsx")
TRc = pd.read_excel("Datasets/2Temporary_Resident_-_Country_of_Citizenship.xlsx")
TRr = pd.read_excel("Datasets/2Temporary_Resident-_Region_of_Citizenship.xlsx")

# Create four columns for data visualizations
viz_col1, viz_col2, viz_col3, viz_col4 = st.columns(4)

with viz_col1:
    st.markdown("### Permanent Resident by Countries")
    st.write("This bar chart compares the 'Count' and 'Base Count' variables from the dataset.")
    fig = px.bar(PRc, x='Count', y='Country', hover_data=[PRc.columns[0], 'Count', 'Base Count'])
    fig.update_layout(height=300, width=350)
    if st.button("Show Chart 1", key="show_chart1_button"):
        st.plotly_chart(fig)
    if st.button("Hide Chart 1", key="hide_chart1_button"):
        pass  # Do nothing

with viz_col2:
    st.markdown("### Permanent Resident by Regions")
    st.write("This bar chart compares the 'Count' and 'Base Count' variables from the dataset.")
    fig = px.bar(PRr, x='Count', y='Region', hover_data=[PRr.columns[0], 'Count', 'Base Count'])
    fig.update_layout(height=300, width=350)
    if st.button("Show Chart 2", key="show_chart2_button"):
        st.plotly_chart(fig)
    if st.button("Hide Chart 2", key="hide_chart2_button"):
        pass  # Do nothing

with viz_col3:
    st.markdown("### Temporary Resident by Regions")
    st.write("This bar chart compares the 'Count' and 'Base Count' variables from the dataset.")
    fig = px.bar(TRr, x='Count', y='Region', hover_data=[TRr.columns[0], 'Count', 'Base Count'])
    fig.update_layout(height=300, width=350)
    if st.button("Show Chart 3", key="show_chart3_button"):
        st.plotly_chart(fig)
    if st.button("Hide Chart 3", key="hide_chart3_button"):
        pass  # Do nothing

with viz_col4:
    st.markdown("### Temporary Resident by Countries")
    st.write("This bar chart compares the 'Count' and 'Base Count' variables from the dataset.")
    fig = px.bar(TRc, x='Count', y='Country', hover_data=[TRc.columns[0], 'Count', 'Base Count'])
    fig.update_layout(height=300, width=350)
    if st.button("Show Chart 4", key="show_chart4_button"):
        st.plotly_chart(fig)
    if st.button("Hide Chart 4", key="hide_chart4_button"):
        pass  # Do nothing
