import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="BakeBuddy Marketplace",
    layout="wide"
)

# ---------- STYLING ----------

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

.subtitle{
text-align:center;
font-size:18px;
color:white;
margin-bottom:30px;
}

.product-card{
background:#F7E7CE;
padding:15px;
border-radius:20px;
box-shadow:0px 4px 10px rgba(0,0,0,0.2);
margin-bottom:25px;
color:black;
}

.price{
font-size:24px;
font-weight:bold;
color:#5a3825;
}

.discount{
color:green;
font-weight:bold;
font-size:18px;
}

.location{
color:#7a4f2c;
font-weight:bold;
}

.timing{
color:#8b4513;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown(
"<div class='title'>BakeBuddy</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Fresh Bakes • Less Waste</div>",
unsafe_allow_html=True
)

# ---------- CART ----------

if "cart" not in st.session_state:
    st.session_state.cart = []

# ---------- LOAD PRODUCTS ----------

if not os.path.exists("inventory.csv"):

    st.error("No products available.")

else:

    inventory = pd.read_csv("inventory.csv")

    if len(inventory) == 0:

        st.warning("No bakery deals available yet.")

    else:

        st.subheader("Tonight's Bakery Deals")

        cols = st.columns(3)

        for index,row in inventory.iterrows():

            with cols[index % 3]:

                st.markdown(
                "<div class='product-card'>",
                unsafe_allow_html=True
                )

                image_path = str(row["Image"])

                if os.path.exists(image_path):

                    st.image(
                        image_path,
                        use_container_width=True
                    )

                st.markdown(
                    f"### {row['Product']}"
                )

                st.write(
                    f"🏪 {row['Bakery']}"
                )

                st.markdown(
                    f"<div class='location'>📍 {row['Location']}</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<div class='timing'>⏰ {row['SaleStart']} - {row['SaleEnd']}</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<div class='price'>₹{row['Price']}</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<div class='discount'>{row['Discount']}% OFF</div>",
                    unsafe_allow_html=True
                )

                st.write(
                    f"Available Quantity: {row['Quantity']}"
                )

                st.info(
                    "Available Tonight Only"
                )

                if st.button(
                    f"Add To Cart {index}",
                    use_container_width=True
                ):

                    st.session_state.cart.append(
                        row.to_dict()
                    )

                    st.success(
                        "Added To Cart"
                    )

                st.markdown(
                "</div>",
                unsafe_allow_html=True
                )

# ---------- CART BUTTON ----------

st.markdown("---")

if st.button(
    "Go To Cart",
    use_container_width=True
):

    st.switch_page(
        "pages/cart.py"
    )