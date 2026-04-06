import streamlit as st
from sales_logic import SolarDataset

data = SolarDataset()

st.set_page_config(page_title="Mierae Solar Sales Machine", page_icon="☀️")
st.title("☀️ Mierae Solar AI Assistant")

lang = st.sidebar.selectbox("Select Language", ["Hindi", "Telugu", "Odia"])
content = data.CONTENT[lang]

st.info(f"**Bot:** {content['greeting']}")

with st.form("lead_form"):
    st.subheader("Quick Qualification")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name")
        bill = st.number_input(f"{content['q_bill']} (₹)", min_value=0)
        city = st.text_input(content['q_city'])
    
    with col2:
        phone = st.text_input("Phone Number")
        house = st.radio(content['q_house'], ["Own House", "Rented"])
        roof = st.radio(content['q_roof'], ["Yes", "No"])

    submitted = st.form_submit_button("Book Free Site Visit")

# --- THE FIXED SALES LOGIC ---
if submitted:
    # Validation: Ensure Name, Phone, City, and Bill are collected [cite: 85, 86, 87, 88, 89]
    if not name or not phone or not city or bill == 0:
        st.error("⚠️ Please fill in all details (Name, Phone, City, and Bill) before booking.")
    
    # Qualification: Check House Type 
    elif house == "Rented":
        st.error("We currently prioritize independent homeowners, but we will contact you for custom options.")
    
    # Qualification: Check Roof Availability [cite: 57]
    elif roof == "Yes":
        st.success(f"Excellent news, {name}! You qualify for the Government Subsidy.")
        st.balloons()
        st.write(f"### {content['pitch']}")
        st.write(f"✅ **Subsidy:** Up to 40% (Max ₹78,000)") [cite: 40, 41]
        st.write(f"✅ **Benefit:** 300 units free electricity/month") [cite: 43]
        st.warning("⚠️ Subsidy limited है! Government scheme अभी चल रही है।") [cite: 82, 83]
    else:
        st.info("Since you don't have roof access, we will contact you to discuss Community Solar projects.")

with st.sidebar.expander("Handling Objections"):
    st.write("**Too Costly?** EMI option available (2k-3k/month)") [cite: 68]
    st.write("**Not Sure?** Free site visit, no commitment") [cite: 70]
    st.write("**No Time?** पूरा process हम manage करेंगे") [cite: 72]
