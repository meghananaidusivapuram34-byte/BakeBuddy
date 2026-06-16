import streamlit as st

st.set_page_config(
    page_title="BakeBuddy",
    page_icon="🥐",
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
font-size:80px;
text-align:center;
color:#FFD27F;
margin-top:10px;
}

.tagline{
font-family:'Poppins',sans-serif;
font-size:22px;
text-align:center;
color:white;
margin-bottom:30px;
}

.hero{
background:rgba(255,255,255,0.08);
padding:25px;
border-radius:20px;
text-align:center;
margin-bottom:30px;
}

.section{
background:#F7E7CE;
padding:20px;
border-radius:20px;
color:black;
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOGO ----------

try:
    st.image(
        "logo.png",
        width=180
    )
except:
    pass

# ---------- TITLE ----------

st.markdown(
"""
<div class='title'>
BakeBuddy
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='tagline'>
Fresh Bakes • Less Waste
</div>
""",
unsafe_allow_html=True
)

# ---------- HERO ----------

st.markdown(
"""
<div class='hero'>

<h2 style='color:white'>
Premium Bakery Marketplace
</h2>

<p style='color:white;font-size:18px'>

Discover fresh bakery products before closing time
and enjoy exclusive discounts while helping local
bakeries reduce food waste.

</p>

</div>
""",
unsafe_allow_html=True
)

# ---------- BANNER ----------

st.image(
"https://images.unsplash.com/photo-1509440159596-0249088772ff",
use_container_width=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- PORTALS ----------

col1,col2 = st.columns(2)

with col1:

    if st.button(
        "Customer Portal",
        use_container_width=True
    ):
        st.switch_page(
            "pages/customer.py"
        )

with col2:

    if st.button(
        "Bakery Partner Portal",
        use_container_width=True
    ):
        st.switch_page(
            "pages/Bakeryowner.py"
        )

# ---------- ABOUT ----------

st.markdown(
"""
<div class='section'>

<h2>
Why BakeBuddy?
</h2>

<p>

Every night, bakeries are left with fresh products
that cannot be sold the next day.

BakeBuddy connects customers with these delicious
items at discounted prices while helping bakeries
recover revenue and reduce food waste.

</p>

</div>
""",
unsafe_allow_html=True
)

# ---------- HOW IT WORKS ----------

st.markdown(
"""
<div class='section'>

<h2>
How It Works
</h2>

<p>

1. Bakery owners upload products available after 9 PM.

<br><br>

2. Customers browse discounted bakery items nearby.

<br><br>

3. Place an order and pick it up before midnight.

<br><br>

4. Save money while reducing food waste.

</p>

</div>
""",
unsafe_allow_html=True
)

# ---------- FOOTER ----------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
"""
<center style='color:white'>

BakeBuddy © 2025

<br>

Fresh Bakes • Less Waste

</center>
""",
unsafe_allow_html=True
)