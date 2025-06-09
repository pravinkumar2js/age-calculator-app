import streamlit as st
from datetime import date

st.title("🎂 Age Calculator App")

birth_date = st.date_input("Your birthdate")

if st.button("Calculate Age"):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    st.success(f"You are {age} years old.")
