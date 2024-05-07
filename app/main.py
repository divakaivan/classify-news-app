from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    class_probs: dict

@app.get('/')
def home():
    return {'health_check': 'OK', 'model_version': model_version}

@app.post('/predict', response_model=PredictionOut)
def predict(payload: TextIn):
    class_probs = predict_pipeline(payload.text)
    return {'class_probs': class_probs}
