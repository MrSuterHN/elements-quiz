import streamlit as st
from quiz_logic import get_random_elements, elements


# App title
st.title("Elements quiz")

# Sidebar navigation
mode = st.sidebar.selectbox("Select Mode", ["Make a Quiz", "Study Elements"])

if mode == "Make a Quiz":
    st.header("Make a Quiz")
    first_n_elements = st.number_input(
        "How many of the first elements would you like to be quizzed on?", 
        min_value=1, 
        max_value=len(elements), step=1,
    )
    elements_in_quiz = st.number_input(
        "How many of the n elements do you want in your quiz?", 
        min_value=1, 
        max_value=first_n_elements, step=1,
    )
    if st.button("Generate Quiz"):
        # Call the function to generate the quiz
        quiz = get_random_elements(elements, first_n_elements, elements_in_quiz)
        st.write(f"Generating quiz for the first {first_n_elements} elements...")
        # Here you would call your function to generate and export the quiz
        # For example:
        # export_quiz_to_file(elements, first_n_elements, elements_in_quiz)
        st.success("Quiz generated successfully!")
