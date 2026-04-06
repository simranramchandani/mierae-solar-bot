import streamlit as st
from sales_logic import SolarDataset

data = SolarDataset()

st.set_page_config(page_title="Mierae Solar Sales Machine", page_icon="☀️")
st.title("☀️ Mierae Solar AI Assistant")

lang = st.sidebar.selectbox("Select Language", ["Hindi", "Telugu", "Odia"])
content = data.CONTENT[lang]

st.info(f"**Bot:** {content['greeting']}") [cite: 47, 48, 49]

with st.form("lead_form"):
    st.subheader("Quick Qualification")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name") [cite: 86]
        # Adding the Rupee sign to the label as discussed
        bill = st.number_input(f"{content['q_bill']} (₹)", min_value=0) [cite: 55, 89]
        city = st.text_input(content['q_city']) [cite: 58, 88]
    
    with col2:
        phone = st.text_input("Phone Number") [cite: 87]
        house = st.radio(content['q_house'], ["Own House", "Rented"]) [cite: 56, 90]
        roof = st.radio(content['q_roof'], ["Yes", "No"]) [cite: 57]

    submitted = st.form_submit_button("Book Free Site Visit") [cite: 16, 74]

# --- THE VALIDATION LAYER ---
if submitted:
    # Check if any text fields are empty
    if not name or not phone or not city or bill == 0:
        st.error("⚠️ Please fill in all details (Name, Phone, City, and Bill) before booking.")
    else:
        # Proceed with Sales Logic only if data is complete
        if house == "Own House" and roof == "Yes":
            st.success(f"Excellent news, {name}! You qualify for the Government Subsidy.") [cite: 38, 40]
            st.balloons()
            st.write(f"### {content['pitch']}") [cite: 59, 62]
            st.write(f"✅ **Subsidy:** {data.SUBSIDY_INFO['percentage']} ({data.SUBSIDY_INFO['max_amount']})") [cite: 40, 41]
            st.write(f"✅ **Benefit:** {data.SUBSIDY_INFO['free_power']}") [cite: 43]
            st.write(f"💰 **Loan:** Interest as low as {data.SUBSIDY_INFO['interest']}") [cite: 45]
            st.warning("⚠️ Subsidy limited है! Government scheme अभी चल रही है।") [cite: 82, 83]
        else:
            # Handling objections for Rented/No Roof
            st.error("We currently prioritize independent homeowners with roof access.") [cite: 56, 57]
            st.info("However, we will contact you at your number to discuss custom solar community options.")
