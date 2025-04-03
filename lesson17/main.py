import streamlit as st

#
# col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
#
# with col1:
#     st.header('column 1')
#     st.write('This is column 1s content')
#
# with col2:
#     st.header('column 2')
#     st.write('This is column 2s content')
#
# with col3:
#     st.header(' column 3')
#     st.write('This is column 3s content')
#
# with col4:
#     st.header(' column 4')
#     st.write('This is column 4s content')
#
# with col5:
#     st.header(' column 5')
#     st.write('This is column 5s content')











with st.form("my_form", clear_on_submit=True):
    name = st.text_input('Name')
    age = st.slider('Age', min_value=0)
    email = st.text_input('Email')
    biography = st.text_area('Enter short bio')
    terms = st.checkbox('I agree to the terms and conditions')
    submit_button = st.form_submit_button(label='Submit')



if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Email: {email}")
    st.write(f"Short bio: {biography}")

    if terms:
        st.write("✅ Agreed on terms and conditions")
    else:
        st.write("❌ Disagreed on terms and conditions")
