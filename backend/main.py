import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load model and columns
model = pickle.load(open('model.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

@app.get('/')
def home():
    return {"messages": "Welcome to the House Price Prediction API!"}

@app.post("/predict")
def predict(data: dict):
    try:
        # convert input data to DataFrame
        df = pd.DataFrame([data])

        # ensure all columns are present
        df = df.reindex(columns=columns, fill_value=0)

        prediction = model.predict(df)

        return {"prediction": float(prediction[0])}
    
    except Exception as e:
        return {"error": str(e)}