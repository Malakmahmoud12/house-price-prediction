from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.app.schemas.prediction import PredictionRequest, PredictionResponse
from backend.app.services.prediction_service import prediction_service

app = FastAPI(title="House Price Prediction API")

# السماح للـ Frontend بالتواصل مع الـ Backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "House Price Prediction API is Running!"}

@app.post("/predict", response_model=PredictionResponse)
def predict_price(request: PredictionRequest):
    try:
        price = prediction_service.predict(
            area_sqft=request.area_sqft,
            bedrooms=request.bedrooms,
            bathrooms=request.bathrooms,
            balcony=request.balcony,
            location=request.location
        )
        return PredictionResponse(predicted_price=price)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))