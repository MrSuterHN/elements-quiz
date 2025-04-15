import streamlit as st
from quiz_logic import elements

st.title("Study Elements")

# Store the starting and ending element numbers in session state
if 'start' not in st.session_state:
    st.session_state.start = 1
if 'end' not in st.session_state:
    st.session_state.end = len(elements)

# Get range of elements
st.session_state.start = st.number_input(
    "Enter the starting element number (e.g., 1 for Hydrogen):", 
    min_value=1, 
    max_value=len(elements), step=1, value=st.session_state.start,
)
st.session_state.end = st.number_input(
    "Enter the ending element number (e.g. 10 for Neon):", 
    min_value=st.session_state.start, 
    max_value=len(elements), step=1, value=st.session_state.end,
)

if st.button("Start Studying"):
    # Store selected elements in session state to persist across reruns
    st.session_state.selected_elements = list(elements.items())[st.session_state.start - 1:st.session_state.end]

# Retrieve selected elements from session state
if "selected_elements" in st.session_state:
    selected_elements = st.session_state.selected_elements

    # Symbol → Name Practice
    st.write("### Symbol → Name Practice:")
    for symbol, name in selected_elements:
        user_answer = st.text_input(f"What is the name for '{symbol}'?", key=f"name_{symbol}")
        if user_answer:
            if user_answer.strip().lower() == name.lower():
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Oops! The correct answer is: {name}")

    # Name → Symbol Practice
    st.write("### Name → Symbol Practice:")
    for symbol, name in selected_elements:
        user_answer = st.text_input(f"What is the symbol for '{name}'?", key=f"symbol_{name}")
        if user_answer:
            if user_answer.strip().lower() == symbol.lower():
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Oops! The correct answer is: {symbol}")