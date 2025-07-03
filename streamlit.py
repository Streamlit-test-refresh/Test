import streamlit as st

st.title("Welcome to Dell Global Business Center ISG NPI")

st.date_input("Transaction Date")
st.radio("Your Department:", ["QA", "NPI", "Process"])
