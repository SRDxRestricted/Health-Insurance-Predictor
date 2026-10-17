import pickle
import pandas as pd

from pathlib import Path
from fastapi import FastAPI
from schemas import InsuranceInput

app = FastAPI(
    title="Health Insurance Premium Predictor",
    description="Predict insurance charges using a trained ML model",
    version="1.0.0"
)

# Load the saved model
MODEL_PATH = (
    Path(__file__).resolve().parent
    / "models"
    / "insurance_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


@app.get("/")
def home():
    return {"message": "Insurance Premium Predictor API is running"}


@app.post("/predict")
def predict_premium(data: InsuranceInput):
    input_df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_df)[0]

    return {
        "predicted_premium": round(float(prediction), 2)
    }