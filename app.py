import streamlit as st
from sales_logic import SolarDataset

# Initialize the logic class
data = SolarDataset()

st.set_page_config(page_title="Mierae Solar Sales Machine", page_icon="☀️")
st.title("☀️ Mierae Solar AI Assistant")

# Define the sidebar for language selection
lang = st.sidebar.selectbox("Select Language", ["Hindi", "Telugu", "Odia"]) [cite: 19]

# CRITICAL FIX: Define 'content' variable right here so it's available for st.info
content = data.CONTENT[lang] 

st.info(f"**Bot:** {content['greeting']}") [cite: 49]

with st.form("lead_form"):
    st.subheader("Quick Qualification") [cite: 13]
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name") [cite: 86]
        # Adding Rupee sign directly to the numeric input label
        bill = st.number_input(f"{content['q_bill']} (₹)", min_value=0) [cite: 55, 89]
        city = st.text_input(content['q_city']) [cite: 58, 88]
    
    with col2:
        phone = st.text_input("Phone Number") [cite: 87]
        house = st.radio(content['q_house'], ["Own House", "Rented"]) [cite: 56, 90]
        roof = st.radio(content['q_roof'], ["Yes", "No"]) [cite: 57]

    submitted = st.form_submit_button("Book Free Site Visit") [cite: 16]

# --- THE VALIDATION & SALES MACHINE LAYER ---
if submitted:
    # 1. First Check: Is everything filled out?
    if not name or not phone or not city or bill == 0: [cite: 85]
        st.error("⚠️ Please fill in all details (Name, Phone, City, and Bill) before we can proceed.")
    
    # 2. Second Check: House Ownership (Your priority)
    elif house == "Rented": [cite: 90]
        st.error("We currently prioritize independent homeowners, but we will call you to discuss solar options for renters.")
    
    # 3. Final Check: High-Quality Lead Close
    elif roof == "Yes": [cite: 57, 94]
        st.success(f"Excellent news, {name}! You are a perfect candidate for the Government Subsidy.") [cite: 11]
        st.balloons()
        st.write(f"### {content['pitch']}") [cite: 62]
        st.write(f"✅ **Subsidy:** {data.SUBSIDY_INFO['percentage']} ({data.SUBSIDY_INFO['max_amount']})") [cite: 40, 41]
        st.write(f"✅ **Monthly Benefit:** {data.SUBSIDY_INFO['free_power']}") [cite: 43]
        st.warning("⚠️ Subsidy limited है! Government scheme अभी चल रही है।") [cite: 82, 83]
    else:
        st.info("Since you don't have roof access, we will contact you to discuss Community Solar projects.")

# Objection Handling Sidebar for Bonus Points
with st.sidebar.expander("Handling Objections"): [cite: 14]
    st.write("**Too Costly?** EMI options available (₹2k-₹3k/month)") [cite: 68]
    st.write("**No Time?** पूरा process हम manage करेंगे") [cite: 72]
