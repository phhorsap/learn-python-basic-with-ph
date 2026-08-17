import streamlit as st

st.title("เครื่องคิดเลข")

a = st.number_input("เลขที่ 1")
b = st.number_input("เลขที่ 2")

if st.button("คำนวณ"):
    st.success(f"ผลรวม = {a+b}")