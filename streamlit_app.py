import streamlit as st
from openai import OpenAI

st.title("Hi there!")

client = OpenAI(
    api_key = ""
)

chat_history = [
    # {"role": "system", "content": "You are a helpful assistant, you can only respond in chinese"},
    {"role": "system", "content": "Please translate all user input into Chinese."}
]

user_input = st.text_input("Enter your message: ")

chat_history.append({"role": "user", "content": user_input})

# sending a request to OpenAI through the OpenAI API
response = client.chat.completions.create(
    model="gpt-4.1",
    # model="gpt-3.5-turbo-0125",
    messages=chat_history,
)

# print the response
st.write(response.choices[0].message.content)
chat_history.append({"role": "assistant", "content": response.choices[0].message.content})
