import streamlit as st

 st.title("User Information form")

def Person(name, surname, age, height, weight):
    name = st.text_input("Enter your name")
    surname = st.text_input("Enter your surname")
    age = st.number_input("Enter your age", min_value=16)
    height = st.number_input("Enter your height", min_value=1.50)
    weight = st.number_input("Enter your weight", min_value=0)

if st.button("Submit Your Info"):
    st.succses("The Information was sent successfully")
    st.write(f"Name: {name}, Surname:{surname},Age {age}, Height: {height}, Weight: {weight}")
Person()

