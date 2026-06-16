import streamlit as st
import pandas as pd
import os

st.title("Create Account")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
address = st.text_area("Address")
city = st.text_input("City")

password = st.text_input(
    "Password",
    type="password"
)

role = st.selectbox(
    "Account Type",
    ["Customer","Bakery Owner"]
)

if st.button("Create Account"):

    new_user = pd.DataFrame([{
        "name":name,
        "email":email,
        "phone":phone,
        "address":address,
        "city":city,
        "password":password,
        "role":role
    }])

    if os.path.exists("users.csv"):

        old = pd.read_csv("users.csv")

        users = pd.concat(
            [old,new_user],
            ignore_index=True
        )

    else:

        users = new_user

    users.to_csv(
        "users.csv",
        index=False
    )

    st.success("Account Created Successfully")