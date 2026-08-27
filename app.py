import streamlit as st
st.title('My first project')
st.header ( " About Me " )
st . subheader ( " Student Information " )
st . write ( " Welcome to my first Streamlit application . " )
st.write ( " Hello Students ! " )
st . text ( " This is normal text . " )
st . markdown ( " ### Python Programming " )
st . write ( " Welcome to Streamlit ! " )

name = st . text_input ( " Enter your name " )
st . write ( " Hello " , name )

age = st.number_input("Enter your age")

st.write("Your age is", age)

marks = st.slider("Select your marks", 0, 100)

st.write("Your marks:", marks)

course = st.selectbox(
    "Select your course",
    ["Python", "Data Science",
     "Machine Learning", "AI"]
)

st.write("You selected:", course)


gender = st.radio(
    "Select your preference",
    ["Male", "female"]
)

st.write("You selected:", gender)


name = st.text_input("Enter your name")

marks = st.number_input(
    "Enter your marks",
    0,
    100
)

if st.button("Check Result"):

    if marks >= 90:
        st.success(f"{name}, you passed!")
    else:
        st.error(f"{name}, you failed!")