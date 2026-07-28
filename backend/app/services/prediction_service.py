import json
import joblib
import numpy as np
import pandas as pd
from backend.app.core.config import settings

# --- حيلة للتوافق الكامل مع إصدارات scikit-learn الحديثة ---
import sklearn.compose._column_transformer
if not hasattr(sklearn.compose._column_transformer, '_RemainderColsList'):
    class _RemainderColsList(list):
        pass
    sklearn.compose._column_transformer._RemainderColsList = _RemainderColsList

import sklearn.impute
if not hasattr(sklearn.impute.SimpleImputer, '_fill_dtype'):
    @property
    def _fill_dtype(self):
        return getattr(self, 'statistics_', None).dtype if hasattr(self, 'statistics_') and self.statistics_ is not None else None
    sklearn.impute.SimpleImputer._fill_dtype = _fill_dtype
# ---------------------------------------------------------

class PredictionService:
    def __init__(self):
        self.model = joblib.load(settings.MODEL_PATH)
        with open(settings.LOCATIONS_PATH, "r") as f:
            self.locations = json.load(f)

    def predict(self, area_sqft: float, bedrooms: int, bathrooms: int, balcony: int, location: str) -> float:
        input_data = pd.DataFrame([{
            "carpet_area_sqft": area_sqft,
            "bedrooms": bedrooms,
            "bathroom": bathrooms,
            "balcony": balcony,
            "location_grouped": location,
            "Transaction": "Resale",
            "Furnishing": "Semi-Furnished",
            "facing": "North",
            "floor_num": 2,
            "Ownership": "Freehold"
        }])

        predicted_log = self.model.predict(input_data)
        predicted_price = np.expm1(predicted_log)[0]
        return float(predicted_price)

prediction_service = PredictionService()