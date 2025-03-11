# 🔍 Sistema de Detecção de Phishing

Este projeto implementa um sistema de **detecção de phishing** utilizando **Machine Learning** e **FastAPI**. O modelo identifica URLs fraudulentas com base em padrões comuns de phishing.

---
## 📌 Tecnologias Utilizadas
- **Python 3.x**
- **FastAPI** (API para prever phishing)
- **Scikit-learn** (modelo de Machine Learning)
- **Pandas & NumPy** (manipulação de dados)
- **Joblib** (armazenamento do modelo treinado)
- **Requests** (coleta de dados)

---
## 🚀 Como Instalar e Rodar o Projeto
### 1️⃣ Clonar o repositório
```bash
  git clone https://github.com/seu-repositorio/phishing-detector.git
  cd phishing-detector
```

### 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)
```bash
  python -m venv venv  # Criar ambiente virtual
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar as dependências
```bash
  pip install -r requirements.txt
```

### 4️⃣ Treinar o modelo (obrigatório antes de rodar a API)
```bash
  python train.py
```
Isso criará o arquivo **phishing_model.pkl**.

### 5️⃣ Rodar a API
```bash
  uvicorn main:app --reload
```
A API ficará disponível em **http://127.0.0.1:8000**.

---
## 🛠 Como Usar a API
### 🔹 Fazer uma previsão
Envie uma requisição POST para `/predict/` com uma lista de URLs:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/predict/' \
-H 'Content-Type: application/json' \
-d '{"urls": ["https://secure-login.bank.com", "https://www.google.com"]}'
```

### 🔹 Resposta esperada:
```json
{
  "predictions": [
    { "url": "https://secure-login.bank.com", "status": "Fraudulenta" },
    { "url": "https://www.google.com", "status": "Legítima" }
  ]
}
```

---
## 📌 Estrutura do Projeto
```
phishing-detector/
│── train.py            # Treina e salva o modelo
│── main.py             # API para detecção de phishing
│── phishing_model.pkl  # Modelo treinado (após rodar train.py)
│── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

---
## 📢 Melhorias Futuras
✅ Adicionar detecção de **e-mails e mensagens fraudulentas**.
✅ Implementar banco de dados para **armazenar histórico de análises**.
✅ Melhorar o modelo com **mais features e fontes de dados**.

---
## 📜 Licença
Este projeto é de uso livre sob a **MIT License**. Contribuições são bem-vindas! 😊