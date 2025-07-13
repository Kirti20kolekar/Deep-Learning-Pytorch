import streamlit as st
import requests

API_URL = "http://localhost:8500/predict"

st.set_page_config(page_title="Multi-Model ML Predictor", layout="centered")
st.title("🧠 Multi-Model ML Predictor")
st.markdown("Use different machine learning models to make predictions.")

# Sidebar - Model selection
model = st.sidebar.selectbox(
    "Choose a model",
    ("knn", "random_forest", "svc", "logistic")
)

# Input form
st.subheader("Enter Feature Values")
num_features = st.number_input("How many features?", min_value=1, max_value=20, value=4)

features = []
for i in range(num_features):
    val = st.number_input(f"Feature {i + 1}", key=f"f_{i}")
    features.append(val)

if st.button("Predict"):
    payload = {
        "features": features,
        "model": model
    }

    try:
        res = requests.post(API_URL, json=payload)
        result = res.json()

        if res.status_code == 200:
            st.success(f"✅ Prediction: {result['prediction']}")
            st.write(f"🧮 Model Used: **{result['model']}**")
        else:
            st.error("⚠️ API Error")
            st.write(result)

    except requests.exceptions.RequestException:
        st.error("❌ Failed to connect to the FastAPI backend. Make sure it is running.")
