from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load all models

models = {"knn":pickle.load(open("knn_model.pkl","rb")),
          "random_forest": pickle.load(open("random_forest_model.pkl", "rb")),
          "svc": pickle.load(open("svc_model.pkl", "rb")),
          "logistic": pickle.load(open("logistic_model.pkl", "rb"))}

# Define input schema

class InputData(BaseModel):

    features: list
    model: str  #'knn', 'random_forest', 'svc', 'logistic'

@app.post('/predict')
def predict(data: InputData):
    model_name = data.model
    features = np.array(data.features).reshape(1,-1)
    if model_name not in models:
        return {"error":"Invalid Model Name"}
    model = models[model_name]
    prediction = model.predict(features)[0]
    return {"model":model_name, "prediction":int(prediction)}