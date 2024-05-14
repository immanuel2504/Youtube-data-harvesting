import streamlit as st
import pandas as pd

# Title of the app
st.title("Youtube Harvesting App")

# Text input widget
name = st.text_input("Enter your name:")

# Display greeting
if name:
    st.write(f"Hello, {name}!")

# Create a simple data frame
data = {
    'Video Title': ['Video 1', 'Video 2', 'Video 3', 'Video 4'],
    'Views': [1500, 2500, 3500, 4500]
}
df = pd.DataFrame(data)

# Display the data frame
st.write("Here are some sample YouTube video data:")
st.write(df)


