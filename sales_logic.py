# The "Brain" of your Mierae Solar Sales Machine
class SolarDataset:
    # Core Knowledge (VERY IMPORTANT) [cite: 36]
    SUBSIDY_INFO = {
        "max_amount": "₹78,000", # [cite: 41]
        "percentage": "Up to 40%", # [cite: 40]
        "free_power": "300 units/month", # [cite: 43]
        "interest": "~6.75%", # [cite: 45]
        "target": "1 crore homes" # [cite: 44]
    }

    # Sales Conversation Flow [cite: 46]
    CONTENT = {
        "Hindi": {
            "greeting": "नमस्ते! क्या आप बिजली बिल कम करना चाहते हैं?", # [cite: 48, 49]
            "pitch": "सरकार अभी 40% तक subsidy दे रही है। 3kW सिस्टम में आपका बिल zero हो सकता है!", # [cite: 60, 62]
            "q_bill": "आपका monthly बिजली बिल कितना आता है?", # [cite: 55]
            "q_house": "क्या आपका खुद का घर है?", # [cite: 56]
            "q_roof": "छत खाली है क्या?", # [cite: 57]
            "q_city": "किस शहर से हैं?", # [cite: 58]
            "close": "क्या मैं आपके लिए free site visit book कर दूं?" # [cite: 74]
        },
        "Telugu": {
            "greeting": "నమస్తే! మీ కరెంట్ బిల్ తగ్గించుకోవాలనుకుంటున్నారా?", # [cite: 50, 51]
            "pitch": "ప్రభుత్వం 40% వరకు subsidy ఇస్తోంది. 25 సంవత్సరాలు almost free electricity.", # [cite: 61, 63, 64]
            "q_bill": "మీ నెలవారీ విద్యుత్ బిల్లు ఎంత?",
            "q_house": "మీకు సొంత ఇల్లు ఉందా?",
            "q_roof": "మీ పైన ఖାళీ స్థలం ఉందా?",
            "q_city": "మీరు ఏ నగరం నుండి వచ్చారు?",
            "close": "నేను మీ కోసం ఉచిత సైట్ సందర్శనను బుక్ చేయవచ్చా?"
        },
        "Odia": {
            "greeting": "ନମସ୍କାର! ଆପଣ ବିଦ୍ୟୁତ ବିଲ୍ କମାଇବାକୁ ଚାହୁଁଛନ୍ତି କି?", # [cite: 52, 53]
            "pitch": "ସରକାର ୪୦% ପର୍ଯ୍ୟନ୍ତ ସବସିଡି ଦେଉଛନ୍ତି।",
            "q_bill": "ଆପଣଙ୍କର ମାସିକ ବିଦ୍ୟୁତ୍ ବିଲ୍ କେତେ?",
            "q_house": "ଆପଣଙ୍କର ନିଜସ୍ୱ ଘର ଅଛି କି?",
            "q_roof": "ଛାତ ଖାଲି ଅଛି କି?",
            "q_city": "ଆପଣ କେଉଁ ସହରରୁ?",
            "close": "ମୁଁ ଆପଣଙ୍କ ପାଇଁ ଏକ ମାଗଣା ସାଇଟ୍ ପରିଦର୍ଶନ ବୁକ୍ କରିପାରିବି କି?"
        }
    }