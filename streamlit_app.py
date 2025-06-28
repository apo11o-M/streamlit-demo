import streamlit as st
from openai import OpenAI

st.title("Hi there!")

# Open the .env file, and read in the api key into a variable
with open(".env", "r") as file:
    open_ai_api_key = file.read()

client = OpenAI(
    api_key = open_ai_api_key
)

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        {"role": "system", "content": "Please translate all user input into Chinese."}
    ]

user_input = st.text_input("Enter your message: ")

st.session_state["chat_history"].append({"role": "user", "content": user_input})

# sending a request to OpenAI through the OpenAI API
response = client.chat.completions.create(
    model="gpt-4.1",
    # model="gpt-3.5-turbo-0125",
    messages=st.session_state["chat_history"],
)

# print the response
st.write(response.choices[0].message.content)
st.session_state["chat_history"].append({"role": "assistant", "content": response.choices[0].message.content})


# Question:
# What are some use cases for the "Session" feature for the application above?
# You have a couple minutes to think about this.

# Practice:
# Modify the 'chat_history' variable so the chat_history list is stored in the streamlit.session_state
