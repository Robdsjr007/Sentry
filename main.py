from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()

# Verifica se o modelo existe antes de carregar
model_path = "phishing_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None  # O modelo precisa ser treinado antes de rodar a API

# Definir esquema da requisição
class URLInput(BaseModel):
    urls: list[str]  # Agora aceita uma lista de URLs

# Função para extrair características de uma URL
def extract_url_features(url):
    return {
        "length": len(url),
        "num_dots": url.count("."),
        "num_slashes": url.count("/"),
        "num_hyphens": url.count("-"),
        "contains_https": int("https" in url),
        "contains_login": int("login" in url),
        "contains_bank": int("bank" in url),
        "contains_secure": int("secure" in url),
        "contains_free": int("free" in url),
        "contains_verify": int("verify" in url)
    }

# Rota para verificar se uma URL é phishing
@app.post("/predict/")
def predict_url(data: URLInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo não encontrado. Treine o modelo primeiro.")

    try:
        results = []
        for url in data.urls:
            features = extract_url_features(url)
            df = pd.DataFrame([features])
            prediction = model.predict(df)[0]
            status = "Fraudulenta" if prediction == 1 else "Legítima"
            results.append({"url": url, "status": status})
        
        return {"predictions": results}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
