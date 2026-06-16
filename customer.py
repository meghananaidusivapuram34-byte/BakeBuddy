import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="BakeBuddy Customer",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Poppins:wght@300;400;500&display=swap');

.stApp{
background:linear-gradient(
135deg,
#2d1b14,
#5a3825,
#d9b382
);
}

.title{
font-family:'Cinzel',serif;
font-size:55px;
text-align:center;
color:#FFD27F;
margin-bottom:10px;
}

.subtitle{
text-align:center;
color:white;
font-size:18px;
margin-bottom:40px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"<div class='title'>BAKEBUDDY</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Customer Login</div>",
unsafe_allow_html=True
)

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button(
    "Login",
    use_container_width=True
):

    if not os.path.exists("users.csv"):

        st.error("No account found. Please create an account first.")

    else:

        users = pd.read_csv("users.csv")

        users.columns = users.columns.str.strip()

        users["email"] = users["email"].astype(str).str.strip()

        users["password"] = users["password"].astype(str).str.strip()

        email = email.strip()

        password = password.strip()

        user = users[
            (users["email"] == email)
            &
            (users["password"] == password)
        ]

        if not user.empty:

            st.session_state.user_name = user.iloc[0]["name"]

            st.session_state.user_email = user.iloc[0]["email"]

            st.session_state.user_phone = user.iloc[0]["phone"]

            st.session_state.user_address = user.iloc[0]["address"]

            st.session_state.user_city = user.iloc[0]["city"]

            st.session_state.user_role = user.iloc[0]["role"]

            st.success("Login Successful")

            st.switch_page(
                "pages/customerdashboard.py"
            )

        else:

            st.error(
                "Invalid Email or Password"
            )

st.markdown("---")

if st.button(
    "Create New Account",
    use_container_width=True
):

    st.switch_page(
        "pages/signup.py"
    )