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
        for i, (symbol, name) in enumerate(quiz.items(), start=1):
            st.write(f"{i}: {symbol} → {name}")
        # Here you would call your function to generate and export the quiz
        # For example:
        # export_quiz_to_file(elements, first_n_elements, elements_in_quiz)
        st.success("Quiz generated successfully!")
elif mode == "Study Elements":
    st.header("Study Elements")
    # Here you would implement the study elements functionality
    start = st.number_input(
        "Enter the starting element number (e.g., 1 for Hydrogen):", 
        min_value=1, 
        max_value=len(elements), step=1,
    )
    end = st.number_input(
        "Enter the ending element number (e.g. 10 for Neon):", 
        min_value=start, 
        max_value=len(elements), step=1,
    )
    if st.button("Start Studying"):
        selected_elements = list(elements.items())[start-1:end]
        st.write("### Symbol → Name Practice:")
        for symbol, name in selected_elements:
            user_answer = st.text_input(f"What is the name for '{symbol}'?", key=f"name_{symbol}")
            if user_answer:
                if user_answer.strip().lower() == name.lower():
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Oops! The correct answer is: {name}")
        
        st.write("### Name → Symbol Practice:")
        for symbol, name in selected_elements:
            user_answer = st.text_input(f"What is the symbol for '{name}'?", key=f"symbol_{name}")
            if user_answer:
                if user_answer.strip().lower() == symbol.lower():
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Oops! The correct answer is: {symbol}")