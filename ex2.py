import streamlit as st

st.title("This is the first application")
st.header("Hello, this is a Streamlit app")
st.subheader("This is a subheader")
st.text("Welcome to the world of Streamlit!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.write(f"Hello, {name}!")

    if st.checkbox("Show Secret Message"):
        st.write("You discovered a hidden message!")

option = st.selectbox(
    "Choose your favorite language:",
    ["Python", "Java", "C++", "JavaScript"]
)

age = st.slider("Select your age", 1, 100, 25)

st.write("Your age is", age)
st.write("You selected:", option)