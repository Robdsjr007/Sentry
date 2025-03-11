import pandas as pd
import numpy as np
import re
import requests
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Coletar dados de phishing (URLs)
def get_phishing_urls():
    response = requests.get("https://openphish.com/feed.txt")
    urls = response.text.split("\n")
    return list(set(filter(None, urls)))  # Remove URLs duplicadas e vazias

# 2. Função para extrair características de URLs
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

# 3. Carregar dados e criar DataFrame
phishing_urls = get_phishing_urls()
phishing_features = [extract_url_features(url) for url in phishing_urls]
df_phishing = pd.DataFrame(phishing_features)
df_phishing["label"] = 1  # 1 = phishing

# 4. Criar dados de URLs legítimos (adicione mais conforme necessário)
legit_urls = [
    "https://www.google.com", "https://www.paypal.com",
    "https://www.bankofamerica.com", "https://www.github.com"
]
legit_features = [extract_url_features(url) for url in legit_urls]
df_legit = pd.DataFrame(legit_features)
df_legit["label"] = 0  # 0 = legítimo

# 5. Unir os datasets
df = pd.concat([df_phishing, df_legit], ignore_index=True)

# 6. Separar treino e teste
X = df.drop(columns=["label"])
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 8. Avaliar o modelo
y_pred = model.predict(X_test)
print("Acurácia:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 9. Salvar o modelo
joblib.dump(model, "phishing_model.pkl")
print("Modelo salvo como phishing_model.pkl")
