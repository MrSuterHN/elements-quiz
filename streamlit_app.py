import streamlit as st
import streamlit.components.v1 as components
from quiz_logic import elements

st.title("Study Elements")

# Store the initial starting and ending element numbers in session state
if 'start' not in st.session_state:
    st.session_state.start = 1
if 'end' not in st.session_state:
    st.session_state.end = len(elements)

# Get range of elements
start = st.number_input("Enter the starting element number (e.g., 1 for Hydrogen):",
    min_value=1,
    max_value=len(elements), step=1, value=st.session_state.start,
)
end = st.number_input(
    "Enter the ending element number (e.g. 10 for Neon):",
    min_value=1,
    max_value=len(elements), step=1, value=st.session_state.end,
)

if st.button("Start Studying"):
    st.session_state.start = start
    st.session_state.end = end
    # Validate the range
    if st.session_state.start > st.session_state.end:
        st.error("Start number must be less than or equal to end number.")
        if "selected_elements" in st.session_state:
            del st.session_state.selected_elements
    else:
        # Store selected elements in session state to persist across reruns
        st.session_state.selected_elements = list(elements.items())[st.session_state.start - 1:st.session_state.end]

# Retrieve selected elements from session state
if "selected_elements" in st.session_state:
    selected_elements = st.session_state.selected_elements

    # Track correct answers
    correct_symbol_to_name = 0
    correct_name_to_symbol = 0
    total_symbol_to_name = len(selected_elements)
    total_name_to_symbol = len(selected_elements)
    all_answered = True
    

    # Symbol → Name Practice
    st.write("### Symbol → Name Practice:")
    for symbol, name in selected_elements:
        user_answer = st.text_input(f"What is the name for '{symbol}'?", key=f"name_{symbol}")
        if user_answer:
            if user_answer.strip().lower() == name.lower():
                st.success("✅ Correct!")
                correct_symbol_to_name += 1
            else:
                st.error(f"❌ Oops! The correct answer is: {name}")

    # Name → Symbol Practice
    st.write("### Name → Symbol Practice:")
    for symbol, name in selected_elements:
        user_answer = st.text_input(f"What is the symbol for '{name}'?", key=f"symbol_{name}")
        if not user_answer:
            all_answered = False
        elif user_answer.strip().lower() == symbol.lower():
            st.success("✅ Correct!")
            correct_name_to_symbol += 1
        else:
            st.error(f"❌ Oops! The correct answer is: {symbol}")
    
    total_questions = correct_name_to_symbol + correct_symbol_to_name

    # Show confetti if all answers are correct
    if (
        all_answered and
        correct_symbol_to_name == total_symbol_to_name and
        correct_name_to_symbol == total_name_to_symbol and
        total_questions > 0
    ):
        st.balloons()
        st.success("🎉 Congratulations! You answered all questions correctly! 🎉")

# reset button
if st.button("Reset"):
    # Clear session state
    st.session_state.clear()
    st.rerun()