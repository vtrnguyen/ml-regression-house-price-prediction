# Regression House Price Prediction

## Overview

This project is a fullstack machine learning web application that predicts house prices based on user input features.

The system includes:

* Machine Learning model (Scikit-learn)
* REST API (FastAPI)
* Frontend UI (Next.js)
* Containerization (Docker)

---

## Tech Stack

### Machine Learning

* Python
* Pandas, NumPy
* Scikit-learn

### Backend

* FastAPI
* Uvicorn

### Frontend

* Next.js (App Router)
* TypeScript
* TailwindCSS

### DevOps

* Docker
* Docker Compose

---

## Features

* Train regression model from Kaggle dataset
* Data preprocessing and feature engineering
* REST API for prediction
* Interactive UI for user input
* Full Dockerized system

---

## Project Structure

```
project/
│
├── backend/
│   ├── main.py
│   ├── model.pkl
│   └── columns.pkl
│
├── frontend/
│   ├── app/
│   └── Dockerfile
│
├── ml/
│   ├── train.py
│   └── data_preprocessing.py
│
├── data/
│   ├── X_clean.csv
│   └── y_clean.csv
│
├── docker-compose.yml
└── README.md
```

---

## How It Works

1. Data is collected and cleaned
2. Model is trained using regression algorithms
3. Model is saved as `.pkl`
4. FastAPI loads model and exposes `/predict` endpoint
5. Frontend sends request and displays prediction

---

## Run Locally (Without Docker)

### Backend

```
cd backend
pip install fastapi uvicorn scikit-learn pandas numpy
python -m uvicorn main:app --reload
```

### Frontend

```
cd frontend
npm install
npm run dev
```

---

## Run With Docker

```
docker-compose up --build
```

Access:

* Frontend: http://localhost:3000
* Backend Docs: http://localhost:8000/docs

---

## Example API Request

POST `/predict`

```
{
  "LotArea": 8450,
  "OverallQual": 7,
  "YearBuilt": 2003
}
```

Response:

```
{
  "prediction": 180000.0
}
```

---

## Author

Vo Trung Nguyen (Origin Dev)
