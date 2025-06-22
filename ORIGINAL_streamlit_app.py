import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

name = st.text_input("Please enter your name:")
age = st.text_input("Please enter your age:")

st.write("Your name is " + name + ", and your age is " + age + ".")

pressed = st.button("Press me!")
if pressed:
    st.write("touch touch")

with st.form("my_form"):
    fav_color = st.selectbox(
        "What's your favorite color?",
        [
            "Red",
            "Orange",
            "Yellow",
            "Green",
            "Blue",
            "Purple"
        ]
    )
    
    reason = st.text_area("Talk about why that's your favorite color.")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("It's interesting that you like " + fav_color + ".")
        st.write("Your say it's because:")
        st.write("""
        ```
        reason
        ```
        """.replace("reason", reason))

