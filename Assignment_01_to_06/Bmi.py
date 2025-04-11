import streamlit as st

st.title("BMI CALCULATOR!")

# Height input from sidebar using a slider
height = st.sidebar.slider("Enter your height (in cm):", 100, 250, 175)

# Weight input from sidebar using a slider
weight = st.sidebar.slider("Enter your weight (in kg):", 40, 200, 70)

# BMI calculation
height_m = height / 100  # convert cm to meters
bmi = weight / (height_m ** 2)

# Display result
st.write(f"Your Height: {height} cm")
st.write(f"Your Weight: {weight} kg")
st.success(f"Your BMI is: {bmi:.2f}")
