import streamlit as st
import requests
import os

# 🔑 Hugging Face token from environment
API_TOKEN = os.getenv("HF_TOKEN")

# ✅ NEW ROUTER API (required now)
API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot (Hugging Face)")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Type your message:")

if user_input:
    st.session_state.chat.append(("You", user_input))

    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        bot_reply = data["choices"][0]["message"]["content"]

    except Exception as e:
        bot_reply = str(data)

    st.session_state.chat.append(("Bot", bot_reply))

# display chat
for role, msg in st.session_state.chat:
    if role == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")