import streamlit as st

if "number" not in st.session_state:
    st.session_state["number"] = 0

click_button = st.button("Add one")
if click_button:
    st.session_state["number"] += 1

st.write(st.session_state["number"])
