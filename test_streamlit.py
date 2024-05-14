import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Function to get SQLAlchemy engine
def get_engine():
    # Encode the '@' symbol in the password
    connection_string = "mysql+mysqlconnector://root:Lourdumary%4010@127.0.0.1/moviesdb"
    engine = create_engine(connection_string)
    return engine

# Function to get data from a specific table
def get_table_data(table_name):
    engine = get_engine()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    engine.dispose()
    return df

# Sidebar for navigation
st.sidebar.title("Navigation")
tab = st.sidebar.selectbox("Select a tab:", ["Home", "Data Extract", "View", "Analysis Using SQL"])

# Home tab
if tab == "Home":
    st.title("Home")
    st.write("Welcome to the Streamlit MySQL Database Viewer.")

# Data Extract tab
elif tab == "Data Extract":
    st.title("Data Extract")
    st.write("Use this tab to extract data from the database.")
    # Example data extraction code
    options = ["actors", "movies"]
    selected_table = st.selectbox("Choose a table to extract:", options)
    if st.button("Extract Data"):
        df = get_table_data(selected_table)
        st.write(f"Data from {selected_table}:")
        st.write(df)

# View tab
elif tab == "View":
    st.title("View")
    st.write("Use this tab to view data from the database.")
    # Example view data code
    options = ["actors", "movies"]
    selected_table = st.selectbox("Choose a table to view:", options)
    df = get_table_data(selected_table)
    st.write(f"Data from {selected_table}:")
    st.write(df)

# Analysis Using SQL tab
elif tab == "Analysis Using SQL":
    st.title("Analysis Using SQL")
    st.write("Use this tab to perform analysis using SQL queries.")
    # Example analysis code
    query = st.text_area("Enter your SQL query here:")
    if st.button("Run Query"):
        engine = get_engine()
        df = pd.read_sql(query, engine)
        engine.dispose()
        st.write("Query Result:")
        st.write(df)



