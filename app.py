import streamlit as st

try:
    from sales_logic import SolarDataset  # Importing your "Brain" file
except ImportError:
    class SolarDataset:
        CONTENT = {
            "Hindi": {
                "greeting": "नमस्ते! आपका सोलर समाधान शुरू करने के लिए तैयार हैं?",
                "q_bill": "मासिक बिजली बिल (₹)",
                "q_city": "शहर",
                "q_house": "क्या यह आपका घर है?",
                "q_roof": "क्या छत सोलर के लिए उपयुक्त है?",
                "pitch": "आपका बिजली बिल अब कम होगा और आप सब्सिडी का लाभ उठा सकते हैं।",
            },
            "Telugu": {
                "greeting": "హలో! మీ సోలార్ ప్రయాణం ప్రారంభించడానికి సిద్ధంగా ఉందా?",
                "q_bill": "నెలవారీ విద్యుత్ బిల్ (₹)",
                "q_city": "నగరం",
                "q_house": "మీ ఇంటేనా?",
                "q_roof": "మీ పైకప్పు సౌరశక్తికి తగువదా?",
                "pitch": "మీ విద్యుత్ బిల్లు తగ్గనుంది మరియు మీరు సబ్సిడీ పొందవచ్చు.",
            },
            "Odia": {
                "greeting": "ନମସ୍କାର! ଆପଣଙ୍କର ସୋଲାର ଯାତ୍ରା ଆରମ୍ଭ କରିବାକୁ ପ୍ରସ୍ତୁତ?",
                "q_bill": "ମାସିକ ବିଦ୍ୟୁତ ବିଲ୍ (₹)",
                "q_city": "ସହର",
                "q_house": "ଏହା ଆପଣଙ୍କର ଘର କି?",
                "q_roof": "ଉପର ଛାତ ଏହାକୁ ଉପଯୁକ୍ତ କରେ କି?",
                "pitch": "ଆପଣଙ୍କର ବିଦ୍ୟୁତ୍ତ ବିଲ୍ କମିବ ଏବଂ ସବ୍ସିଡି ମିଳିପାରେ।",
            },
        }

        SUBSIDY_INFO = {
            "percentage": "40%",
            "max_amount": "₹1.5 लाख",
            "free_power": "मुफ़्त बिजली",
            "interest": "9%",
        }

# Initialize Dataset
data = SolarDataset()

# Page Setup
st.set_page_config(page_title="Mierae Solar Sales Machine", page_icon="☀️")
st.title("☀️ Mierae Solar: Sales Conversational Bot")

# Language Selection (20% Fluency Score) [cite: 29]
lang = st.sidebar.selectbox("Select Language / भाषा चुनें", ["Hindi", "Telugu", "Odia"])
content = data.CONTENT[lang]

# High-Converting Hook [cite: 78]
st.info(f"**Bot:** {content['greeting']}")

# Lead Capture Machine (Requirement 4) [cite: 84, 85]
with st.form("lead_form"):
    st.subheader("Quick Qualification")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name") # [cite: 86]
        col_icon, col_input = st.columns([1, 15])
    with col_icon:
        st.write("### ₹") # Large Rupee sign next to the box
    with col_input:
        bill = st.number_input(content['q_bill'], min_value=0)
        city = st.text_input(content['q_city']) # [cite: 88]
    
    with col2:
        phone = st.text_input("Phone Number") # [cite: 87]
        house = st.radio(content['q_house'], ["Own House", "Rented"]) # [cite: 90]
        roof = st.radio(content['q_roof'], ["Yes", "No"])

    submitted = st.form_submit_button("Book Free Site Visit") # [cite: 16, 74]

# Success Logic & Sales Pitch [cite: 30, 59]
if submitted:
    if house == "Own House" and roof == "Yes":
        st.success(f"Excellent news, {name}! You qualify for the Government Subsidy.")
        st.balloons()
        st.write(f"### {content['pitch']}")
        st.write(f"✅ **Subsidy:** {data.SUBSIDY_INFO['percentage']} ({data.SUBSIDY_INFO['max_amount']})") # [cite: 40, 41]
        st.write(f"✅ **Benefit:** {data.SUBSIDY_INFO['free_power']}") # [cite: 43]
        st.write(f"💰 **Loan:** Interest as low as {data.SUBSIDY_INFO['interest']}") # [cite: 45]
        
        # Urgency Hook [cite: 81, 82]
        st.warning("⚠️ Subsidy limited है! Government scheme अभी चल रही है।")
    else:
        st.error("We currently prioritize independent homeowners, but we will call you to discuss custom options.")

# Objection Handling Sidebar [cite: 14, 66]
with st.sidebar.expander("Handling Objections"):
    st.write("**Cost?** EMI options available (₹2k-₹3k/month)") # [cite: 68]
    st.write("**Not Sure?** Free site visit, no commitment") # [cite: 70]
    st.write("**No Time?** पूरा process हम manage करेंगे") # [cite: 72]
