import streamlit as st
import pandas as pd

# Load your data from the specific sheet in the Excel file
data = pd.read_excel('JD tags1.xlsx', sheet_name='job_tags_model_test_output_old1')

# Title of the app
st.title('Output Data Viewer')

# Display the data
st.write(data)

# Optionally, you can add other features like filtering, charts, etc.

