import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

MODEL_PATH = Path(__file__).parent / "heart_svc_trained_model.pkl"


@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


model = load_model()

st.title("❤️ Heart Disease Prediction System")
st.markdown(
    """
This teaching app predicts heart disease status using a model trained on the
UCI Cleveland heart disease dataset.

Target labels:
- `0` = No heart disease
- `1` = Heart disease present
"""
)

st.divider()

col1, col2 = st.columns(2)
with col1:
    cp = st.selectbox("Chest Pain Type (cp)", [1, 2, 3, 4], index=3)
    thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=60, max_value=220, value=150)
with col2:
    exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1], index=0)
    oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)

if st.button("Predict Heart Disease", type="primary", use_container_width=True):
    user_input = pd.DataFrame(
        {
            "cp": [cp],
            "thalach": [float(thalach)],
            "exang": [exang],
            "oldpeak": [float(oldpeak)],
        }
    )

    prediction = int(model.predict(user_input)[0])

    st.divider()
    if prediction == 1:
        st.error("### ⚠️ HEART DISEASE PRESENT")
    else:
        st.success("### ✅ NO HEART DISEASE")

    with st.expander("See the feature vector sent to the model"):
        st.dataframe(user_input, hide_index=True)

st.divider()
st.caption(
    "For educational use only. This is not a medical diagnosis tool."
)
