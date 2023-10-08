import streamlit as st
import openai
import pandas as pd
import time


import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import time  # to simulate a real time data, time loop

# Set the OpenAI API Key (Replace 'XXXXXXXXXXXXX' with your actual API key)
openai.api_key = 'XXXXXXXXXXXXX'
# Create a Streamlit app with improved design
st.set_page_config(page_title="AI-Powered Business Idea Generator", layout="wide")
# Custom CSS to style the app
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
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
    </style>
    """,
    unsafe_allow_html=True
)

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

# Header
st.title("AI-Powered Business Idea Generator")
st.write("Welcome to the AI-powered Business Idea Generator. Our AI model has analyzed data from various countries and industries to provide you with unique business ideas.")
st.write("Simply select a country, and we'll use the power of AI to suggest business ideas tailored to people from that country living in your chosen location.")

# Sidebar for user input
st.sidebar.header("Select Options")
country = st.sidebar.selectbox("Select Country", df['Country'])
countryOfResidence = st.sidebar.text_input("Enter Country of Residence", "Canada")

# Main content area
st.write("Country with max percentage:", specific_country_max_percentage['Country'])
st.write("Percentage:", specific_country_max_percentage['Percentage'])
st.write("Base Count:", specific_country_max_percentage['Base Count'])

# Button to generate the business idea
if st.button("Generate Business Idea"):
    idea = get_business_idea(country, countryOfResidence)
    st.write("Business idea for people from", country, "living in", countryOfResidence, ":")
    st.write(idea)


#DataViz
PRc = pd.read_excel("Datasets/2Permanent_Resident_-_Country_of_Citizenship copy.xlsx")
PRr = pd.read_excel("Datasets/2Permanent_Resident_-_Region_of_Citizenship.xlsx")
TRc = pd.read_excel("Datasets/2Temporary_Resident_-_Country_of_Citizenship.xlsx")
TRr = pd.read_excel("Datasets/2Temporary_Resident-_Region_of_Citizenship.xlsx")

st.header("Permanent Residents")
# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    #Perment resident by countries
    PRc = PRc.sort_values(by='Count', ascending=True)
    st.markdown("### Population Denisity via Ethnicity'")
    st.write("This scatter plot compares the 'Count' and 'Base Count' variables from the dataset.")

    fig = px.bar(PRc, x='Count', y='Country', hover_data=[PRc.columns[0], 'Count', 'Base Count'])
    fig.update_layout(height=300, width=500)  

    st.plotly_chart(fig)
    
   

with fig_col2:
    #PRr = PRr.sort_values(by='Count', ascending=True)
    #temporary resident by regions
    st.markdown("### Population Denisity via Ethnicity'")
    st.write("This scatter plot compares the 'Count' and 'Base Count' variables from the dataset.")

    fig = px.bar(TRr, x='Count', y='Region', hover_data=[TRr.columns[0], 'Count', 'Base Count'])
    fig.update_layout(height=300, width=500)  

    st.plotly_chart(fig)

st.header("Temporary Residents")
# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    #PRr = PRr.sort_values(by='Count', ascending=True)
    #permenent resident by regions
    st.markdown("### Population Denisity via Ethnicity'")
    st.write("This scatter plot compares the 'Count' and 'Base Count' variables from the dataset.")

    fig = px.bar(PRr, x='Count', y='Region', hover_data=[PRr.columns[0], 'Count', 'Base Count'])
    fig.update_layout(height=300, width=500)  

    st.plotly_chart(fig)
    

with fig_col2:
    #temporary resident by countries
    TRc = TRc.sort_values(by='Count', ascending=True)
    st.markdown("### Population Denisity via Ethnicity'")
    st.write("This scatter plot compares the 'Count' and 'Base Count' variables from the dataset.")

    fig = px.bar(TRc, x='Count', y='Country', hover_data=[TRc.columns[0], 'Count', 'Base Count'])
    fig.update_layout(height=300, width=500)  

    st.plotly_chart(fig)
