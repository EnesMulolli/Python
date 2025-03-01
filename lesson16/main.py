import streamlit as st

from lesson4.loops import user_input


#pip install streamlit
#run streamlit folder/file.py

def main():
    st.title('Hello World!')

if __name__ == '__name_':
    main()

if st.button("Click Me"):
    st.write("Button clicked")

st.checkbox("check me!")

if st.checkbox("Check me to show some text!"):
    st.write("This text was showed because u clicked the xheckbox")


user_input = st.text_input("Text input", "Write somethin")
st.write("The text you wrote is:", user_input)

age = st.number_input("Enter your age", min_value=1,  max_value=100)
st.write(f"Your age is:{age}")


message = st.text_area("Enter some text")
st.write(f"Your text: {message}")


choice = st.radio("Pick one",['choice 1', 'choice 2', 'choice 3'])
st.write(f"You chose:{choice}")


if st.button("Sucsess"):
    st.sucsess("It was sent sucsesfylly")

try:
    1 / 0

except Exception as e:
    st.exeption(e)




























