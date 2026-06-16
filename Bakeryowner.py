import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.stApp{
background:linear-gradient(135deg,#2d1b14,#5a3825,#d9b382);
}
h1{
color:#ffd27f;
text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("BakeBuddy Partner Login")

email=st.text_input("Email")
password=st.text_input("Password",type="password")

if st.button("Login"):
    st.success("Login Successful")
    st.switch_page("pages/Bakeryownerdashboard.py")