from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
import numpy as np

app = FastAPI()
#https://abramuhara-fast-api.hf.space/predict/ adresi uygunsuzluk 
#https://abramuhara-fast-api.hf.space/predict-age/ 'e atılan post verilerden muhtemel yaş kategorisini verir
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("AbraMuhara/Fine-TunedBERTURKOfansifTespit")
model = AutoModelForSequenceClassification.from_pretrained("AbraMuhara/Fine-TunedBERTURKOfansifTespit")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import catboost
from huggingface_hub import hf_hub_download
app = FastAPI()


catboost_model = catboost.CatBoostClassifier().load_model(hf_hub_download("AbraMuhara/AgeClassificationTDDI2024", "best_catboost_model.cbm"))
label_encoder = joblib.load(hf_hub_download("AbraMuhara/AgeClassificationTDDI2024", "label_encoder.pkl"))

class TextInput(BaseModel):
    text: str

class AgeInput(BaseModel):
    features: list[float]  # 15 özellik içeren liste

@app.get('/')
def home():
    return {"hello": "Bitfumes"}


@app.post("/predict/")
async def predict(input: TextInput):
    try:
        inputs = tokenizer(input.text, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=-1).item()
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict-age/")
async def predict_age(input: AgeInput):
    try:
        # Özelliklerin numpy dizisine dönüştürülmesi
        features_array = np.array(input.features).reshape(1, -1)
        
        # Tahmin yapma
        prediction = catboost_model.predict(features_array)
        
        # Etiketleri geri dönüştürme
        decoded_prediction = label_encoder.inverse_transform(prediction)[0]

        return {"age_group": decoded_prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
