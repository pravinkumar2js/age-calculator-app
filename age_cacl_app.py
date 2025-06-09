import streamlit as st
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

st.title("📅 Michel Advanced Age Calculator")

min_date = date(1900,1,1)
today = date.today()
# Inputs
dob = st.date_input("Enter your Date of Birth", min_value=min_date, max_value=today)
target = st.date_input("Calculate age at this date", value=datetime.today())

if dob > target:
    st.error("❌ Date of birth cannot be after the target date.")
else:
    rd = relativedelta(target, dob)
    delta = target - dob
    total_days = delta.days

    # Breakdown
    years = rd.years
    months = rd.months
    days = rd.days
    weeks = total_days // 7
    week_days = total_days % 7
    hours = total_days * 24
    minutes = hours * 60
    seconds = minutes * 60

    # Output
    st.subheader("🧮 Age Difference")
    st.write(f"**{years} years, {months} months, {days} days**")
    st.write(f"or **{years * 12 + months} months, {days} days**")
    st.write(f"or **{weeks} weeks, {week_days} days**")
    st.write(f"or **{total_days:,} days**")
    st.write(f"or **{hours:,} hours**")
    st.write(f"or **{minutes:,} minutes**")
    st.write(f"or **{seconds:,} seconds**")
