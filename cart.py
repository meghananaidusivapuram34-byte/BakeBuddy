import streamlit as st

st.set_page_config(
    page_title="BakeBuddy Cart",
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
font-size:50px;
text-align:center;
color:#FFD27F;
}

.cart-box{
background:#F7E7CE;
padding:15px;
border-radius:15px;
margin-bottom:15px;
color:black;
}

.total{
font-size:28px;
font-weight:bold;
color:#FFD27F;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"<div class='title'>BakeBuddy Cart</div>",
unsafe_allow_html=True
)

if "cart" not in st.session_state:
    st.session_state.cart = []

if len(st.session_state.cart) == 0:

    st.warning("Your cart is empty")

else:

    total = 0

    for i,item in enumerate(st.session_state.cart):

        final_price = (
            item["Price"]
            -
            (
                item["Price"]
                * item["Discount"]
                /100
            )
        )

        total += final_price

        st.markdown(
        "<div class='cart-box'>",
        unsafe_allow_html=True)

        col1,col2 = st.columns([1,2])

        with col1:

            if str(item["Image"]):
                st.image(
                    item["Image"],
                    width=150
                )

        with col2:

            st.subheader(
                item["Product"]
            )

            st.write(
                item["Bakery"]
            )

            st.write(
                f"₹{final_price:.0f}"
            )

            if st.button(
                f"Remove {i}"
            ):

                st.session_state.cart.pop(i)

                st.rerun()

        st.markdown(
        "</div>",
        unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
    f"<div class='total'>Total : ₹{total:.0f}</div>",
    unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "Proceed To Payment",
        use_container_width=True
    ):
        st.session_state.total_amount = total

        st.switch_page(
            "pages/payment.py"
        )