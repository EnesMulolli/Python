import streamlit as st

st.title("User Information Form")

# Function to get user input
def person():
    name = st.text_input("Enter your name")
    surname = st.text_input("Enter your surname")
    age = st.number_input("Enter your age", min_value=16)
    height = st.number_input("Enter your height (in meters)", min_value=1.50)
    weight = st.number_input("Enter your weight (in kg)", min_value=0.0)

    return name, surname, age, height, weight

# Get input values
name, surname, age, height, weight = person()

# Button to submit information
if st.button("Submit Your Info"):
    st.success("The information was sent successfully!")
    st.write(f"**Name:** {name}")
    st.write(f"**Surname:** {surname}")
    st.write(f"**Age:** {age}")
    st.write(f"**Height:** {height} meters")
    st.write(f"**Weight:** {weight} kg")
