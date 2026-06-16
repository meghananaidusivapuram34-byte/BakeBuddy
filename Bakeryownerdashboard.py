import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(
    page_title="BakeBuddy Partner Studio",
    layout="wide"
)

# ---------------- STYLING ----------------

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
color:white;
font-size:18px;
}

.card{
background:#F7E7CE;
padding:20px;
border-radius:20px;
margin-bottom:20px;
color:black;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
"<div class='title'>BakeBuddy</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='subtitle'>Partner Studio</div>",
unsafe_allow_html=True
)

st.markdown("---")

# ---------------- FILE SETUP ----------------

if not os.path.exists("inventory.csv"):

    pd.DataFrame(
        columns=[
            "Bakery",
            "Product",
            "Price",
            "Quantity",
            "Discount",
            "Location",
            "SaleStart",
            "SaleEnd",
            "Image"
        ]
    ).to_csv(
        "inventory.csv",
        index=False
    )

# ---------------- ADD PRODUCT ----------------

st.subheader("Add Product")

bakery = st.text_input(
    "Bakery Name"
)

location = st.text_input(
    "Bakery Location"
)

product = st.text_input(
    "Product Name"
)

price = st.number_input(
    "Original Price",
    min_value=1
)

quantity = st.number_input(
    "Quantity Available",
    min_value=1
)

discount = st.number_input(
    "Discount %",
    min_value=0,
    max_value=90
)

sale_start = st.time_input(
    "Sale Starts",
    value=datetime.strptime(
        "21:00",
        "%H:%M"
    ).time()
)

sale_end = st.time_input(
    "Sale Ends",
    value=datetime.strptime(
        "23:59",
        "%H:%M"
    ).time()
)

image = st.file_uploader(
    "Upload Product Image",
    type=["jpg","jpeg","png"]
)

if st.button(
    "Add Product",
    use_container_width=True
):

    if (
        bakery and
        location and
        product and
        image
    ):

        os.makedirs(
            "uploads",
            exist_ok=True
        )

        image_path = os.path.join(
            "uploads",
            image.name
        )

        with open(
            image_path,
            "wb"
        ) as f:

            f.write(
                image.getbuffer()
            )

        inventory = pd.read_csv(
            "inventory.csv"
        )

        new_row = pd.DataFrame(
            [[
                bakery,
                product,
                price,
                quantity,
                discount,
                location,
                str(sale_start),
                str(sale_end),
                image_path
            ]],
            columns=[
                "Bakery",
                "Product",
                "Price",
                "Quantity",
                "Discount",
                "Location",
                "SaleStart",
                "SaleEnd",
                "Image"
            ]
        )

        inventory = pd.concat(
            [
                inventory,
                new_row
            ],
            ignore_index=True
        )

        inventory.to_csv(
            "inventory.csv",
            index=False
        )

        st.success(
            "Product Added Successfully!"
        )

# ---------------- PRODUCT LIST ----------------

st.markdown("---")

st.subheader(
    "Products Uploaded"
)

inventory = pd.read_csv(
    "inventory.csv"
)

if len(inventory) > 0:

    for i,row in inventory.iterrows():

        st.markdown(
        "<div class='card'>",
        unsafe_allow_html=True)

        col1,col2 = st.columns(
            [1,2]
        )

        with col1:

            if os.path.exists(
                str(row["Image"])
            ):
                st.image(
                    row["Image"],
                    width=180
                )

        with col2:

            st.subheader(
                row["Product"]
            )

            st.write(
                f"Bakery: {row['Bakery']}"
            )

            st.write(
                f"Location: {row['Location']}"
            )

            st.write(
                f"Price: ₹{row['Price']}"
            )

            st.write(
                f"Discount: {row['Discount']}%"
            )

            st.write(
                f"Quantity: {row['Quantity']}"
            )

            st.write(
                f"Sale Timing: {row['SaleStart']} - {row['SaleEnd']}"
            )

        st.markdown(
        "</div>",
        unsafe_allow_html=True)