from enum import unique

import pandas as pd
import streamlit as st
import plotly.express as px


st.header("Displaying dataframes")

# Create a sample DataFrame using a dictionary
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})

# Display the DataFrame in the Streamlit app as an interactive table
st.dataframe(data)

# Load the dataset
books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

# Streamlit app title and description
st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling books from 2009 to 2022.")

st.sidebar.header("Add New Book Data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.slider("User Rating", 0.5,5.0, 0.0, 0.1)
    new_review = st.number_input('Review', min_value=0, step=1)
    new_price = st.number_input('Price', min_value=0, step=1)
    new_year = st.number_input('Year', min_value=2009, max_value=2022, step=1)
    new_Genre = st.selectbox("Genre", books_df['Genre'].unique())
    submit_button = st.form_submit_button(label="Add Book")

if  submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating':  new_user_rating,
        'Reviews': new_review,
        'Price': new_price,
        'Year': new_year,
        'Genre':  new_Genre
    }
    books_df = pd.concat([pd.DataFrame(new_data, index=[0]), books_df], ignore_index=True)
    books_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)
    st.sidebar.success("New Book Added Successfully!")

st.sidebar.header("Filter Options")
selected_author = st.sidebar.selectbox("Select Author", ['All'] +list(books_df['Author'].unique()))
selected_Year = st.sidebar.selectbox("Select Year", ['All'] + list(books_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre", ['All'] + list(books_df['Genre'].unique()))
min_rating = st.sidebar.slider("Minimum User Rating", 0.0, 5.0, 0.0, 0.1)
max_price = st.sidebar.slider("Maximum Price", 0, books_df['Price'].max(), books_df['Price'].max())

filtered_Book_df = books_df.copy()

if selected_author != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Author'] == selected_author]
if selected_Year != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Year'] == selected_Year]
if selected_genre != "All":
    filtered_Book_df = filtered_Book_df[filtered_Book_df['Genre'] == selected_genre]

filtered_Book_df =  filtered_Book_df[( filtered_Book_df['User Rating'] >= min_rating) & filtered_Book_df['Price'] <= max_price]

# Summary Statistics
st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

# Display summary statistics in a row of metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")

# Dataset Preview
st.subheader("Dataset Preview")
st.write(books_df.head())

# Book Title Distribution and Author Distribution
col1, col2 = st.columns(2)

# Book title distribution
with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

# Author distribution
with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

# Genre Distribution Pie Chart
st.subheader("Genre Distribution")
fig = px.pie(books_df, names='Genre', title='Most Liked Genre (2009-2022)', color='Genre',
             color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction vs Non-Fiction Books Over the Years")
size = books_df.groupby(['Year', 'Genre']).size().reset_index(name='Count')
fig = px.bar(size, x='Year', y='Count',color='Genre', title='Number of Fiction vs Non-Fiction Books from 2009-2022',
             color_discrete_sequence=px.colors.sequential.Plasma, barmode='group')
st.plotly_chart(fig)

st.header('Top 15 Authors by Counts of Books Over the Years')
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']
fig = px.bar(top_authors, x='Count', y='Author', orientation='h',
             title='Top 15 Authors by Counts of Books Published',
             labels={'Count': 'Counts of Books Published', 'Author':'Author'},
             color='Count', color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Filter Data by Genre")
genre_filter = st.selectbox('Select Genre', books_df['Genre'].unique())
filter_df = books_df[books_df['Genre'] == genre_filter]
st.write(filter_df)