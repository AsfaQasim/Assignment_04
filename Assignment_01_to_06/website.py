import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  

st.title("Simple Data Dashboard")

# File upload section
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Data preview
    st.subheader("Data Preview")
    st.write(df.head())

    # Data summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # Data filtering
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_value = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_value)
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Plotting
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        try:
            plot_data = filtered_df.set_index(x_column)[y_column]
            st.line_chart(plot_data)
        except Exception as e:
            st.error(f"Error generating plot: {e}")
else:
    st.info("Please upload a CSV file to view the data.")
