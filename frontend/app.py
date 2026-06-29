import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/process-email"

st.set_page_config(
    page_title="Agentic AI Banking",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Agentic AI Banking Email Processing System")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    customer_id = st.number_input(
        "Customer ID",
        min_value=100000,
        value=100000
    )

    subject = st.text_input(
        "Email Subject",
        value="Card Charged Twice"
    )

with col2:
    body = st.text_area(
        "Email Body",
        value="My card was charged twice yesterday. Please help.",
        height=150
    )

st.markdown("---")

if st.button("🚀 Process Email", use_container_width=True):

    payload = {
        "customer_id": int(customer_id),
        "subject": subject,
        "body": body
    }

    try:

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()

            st.success("Email Processed Successfully!")

            st.markdown("## 🎫 Ticket")

            st.json(result["ticket"])

            st.markdown("## 🤖 Confidence Agent")

            st.json(result["confidence"])

            st.markdown("## 🧠 Novelty Agent")

            st.json(result["novelty"])

            st.markdown("## 👤 Customer Context")

            st.json(result["customer"])

            st.markdown("## 📜 Policy")

            st.json(result["policy"])

            st.markdown("## ✅ Decision")

            st.json(result["decision"])

        else:

            st.error(response.text)

    except Exception as e:

        st.error(str(e))