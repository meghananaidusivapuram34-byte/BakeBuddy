import streamlit as st
from datetime import datetime, timedelta
import random

st.set_page_config(
    page_title="BakeBuddy Checkout",
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
}

.card{
background:#F7E7CE;
padding:20px;
border-radius:20px;
color:black;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"<div class='title'>BakeBuddy Checkout</div>",
unsafe_allow_html=True
)

# ---------------- TOTAL ----------------

amount = st.session_state.get(
    "total_amount",
    0
)

st.markdown(
f"""
<div class='card'>
<h2>Total Amount : ₹{amount:.0f}</h2>
</div>
""",
unsafe_allow_html=True
)

# ---------------- CUSTOMER PROFILE ----------------

customer_name = st.session_state.get(
    "user_name",
    "Customer"
)

phone = st.session_state.get(
    "user_phone",
    ""
)

address = st.session_state.get(
    "user_address",
    ""
)

city = st.session_state.get(
    "user_city",
    ""
)

st.subheader("Delivery Details")

st.info(
    f"""
Name: {customer_name}

Phone: {phone}

Address: {address}

City: {city}
"""
)

edit_address = st.checkbox(
    "Use Different Address"
)

if edit_address:

    address = st.text_area(
        "New Address"
    )

    city = st.text_input(
        "City"
    )

# ---------------- PAYMENT ----------------

st.subheader("Payment Method")

payment_method = st.radio(
    "",
    [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Cash On Delivery"
    ]
)

if payment_method == "UPI":

    st.text_input(
        "UPI ID"
    )

elif payment_method in [
    "Credit Card",
    "Debit Card"
]:

    st.text_input(
        "Card Number"
    )

    st.text_input(
        "Card Holder Name"
    )

    st.text_input(
        "CVV",
        type="password"
    )

# ---------------- ORDER ----------------

if st.button(
    "Place Order",
    use_container_width=True
):

    order_id = random.randint(
        10000,
        99999
    )

    delivery_time = (
        datetime.now()
        + timedelta(minutes=45)
    )

    st.success(
        "Order Placed Successfully!"
    )

    st.balloons()

    st.markdown(f"""

# Order Confirmed

### Order Number
#{order_id}

### Customer
{customer_name}

### Payment Method
{payment_method}

### Delivery Address

{address}

{city}

### Estimated Arrival

{delivery_time.strftime('%I:%M %p')}

---

*"Freshly baked. Carefully delivered."*

Thank you for choosing BakeBuddy.
""")

    st.session_state.cart = []