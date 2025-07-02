import streamlit as st
import requests

st.title("SmartSDLC – AI-Powered Assistant")

query = st.text_input("Enter your prompt:")

if st.button("Submit"):
    response = requests.post("http://localhost:8000/process/", json={"query": query})
    result = response.json().get("result", "")
    st.write(f"AI Response: {result}")
