# Heart Disease Predictor - Streamlit App

This app predicts whether heart disease is present (`1`) or absent (`0`) using a model trained in:

- `../2 - Heart Disease Prediction/Heart_Disease_Prediction_Recommended.ipynb`

## Run Locally

```bash
cd streamlit-heart-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The app opens at http://localhost:8501.

## Deploy (Streamlit Community Cloud)

- Repository: this repo
- Branch: main
- Main file path: `streamlit-heart-app/app.py`
