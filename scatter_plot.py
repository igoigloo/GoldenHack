import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache
def load_data():
    file_path = 'current_trade_area_data.xlsx'
    df = pd.read_excel(file_path)
    df = df.dropna(subset=['Count', 'Base Count'])  # Drop rows with NaN values in these columns
    
    # Exclude the row with the max Base Count
    max_base_count = df['Base Count'].max()
    df = df[df['Base Count'] < max_base_count]
    
    return df

# Load the cleaned data
df = load_data()

# Streamlit app
st.title('Scatter Plot of Count vs Base Count Excluding Max Base Count')
st.write("This scatter plot compares the 'Count' and 'Base Count' variables from the dataset, excluding the max Base Count.")

# Create a scatter plot
fig = px.scatter(df, x='Count', y='Base Count', hover_data=[df.columns[0], 'Count', 'Base Count'])

# Display the scatter plot
st.plotly_chart(fig)