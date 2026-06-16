import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="BakeBuddy Admin",
    layout="wide"
)

# ---------------- PAGE TITLE ----------------

st.title("BakeBuddy Admin Dashboard")
st.caption("Business Insights & Platform Overview")

# ---------------- LOAD FILES ----------------

if os.path.exists("inventory.csv"):
    inventory = pd.read_csv("inventory.csv")
else:
    inventory = pd.DataFrame()

if os.path.exists("users.csv"):
    users = pd.read_csv("users.csv")
else:
    users = pd.DataFrame()

# ---------------- CALCULATIONS ----------------

products_listed = len(inventory)

active_bakeries = 0
if not inventory.empty and "Bakery" in inventory.columns:
    active_bakeries = inventory["Bakery"].nunique()

total_customers = 0
if not users.empty and "role" in users.columns:
    total_customers = len(
        users[
            users["role"].astype(str).str.lower()
            == "customer"
        ]
    )

potential_revenue = 0
if (
    not inventory.empty
    and "Price" in inventory.columns
    and "Quantity" in inventory.columns
):
    potential_revenue = (
        inventory["Price"] *
        inventory["Quantity"]
    ).sum()

food_saved = 0
if (
    not inventory.empty
    and "Quantity" in inventory.columns
):
    food_saved = inventory["Quantity"].sum()

# ---------------- KPI CARDS ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Products Listed",
        products_listed
    )

with col2:
    st.metric(
        "Active Bakeries",
        active_bakeries
    )

with col3:
    st.metric(
        "Customers",
        total_customers
    )

with col4:
    st.metric(
        "Potential Revenue",
        f"₹{potential_revenue:,.0f}"
    )

st.divider()

# ---------------- BUSINESS IMPACT ----------------

st.subheader("Business Impact")

col1, col2 = st.columns(2)

with col1:
    st.info(
        f"Food Items Saved From Waste: {food_saved}"
    )

with col2:
    st.success(
        f"Partner Bakeries: {active_bakeries}"
    )

st.divider()

# ---------------- INVENTORY ----------------

st.subheader("Inventory Overview")

if not inventory.empty:

    st.dataframe(
        inventory,
        use_container_width=True
    )

else:

    st.warning(
        "No products uploaded yet."
    )

st.divider()

# ---------------- USERS ----------------

st.subheader("Registered Users")

if not users.empty:

    st.dataframe(
        users,
        use_container_width=True
    )

else:

    st.warning(
        "No users registered yet."
    )

st.divider()

# ---------------- TOP PRODUCT ----------------

st.subheader("Top Product")

if (
    not inventory.empty
    and "Price" in inventory.columns
):

    highest = inventory.loc[
        inventory["Price"].idxmax()
    ]

    st.success(
        f"""
Product: {highest['Product']}

Bakery: {highest['Bakery']}

Price: ₹{highest['Price']}
"""
    )

else:

    st.info(
        "No products available."
    )