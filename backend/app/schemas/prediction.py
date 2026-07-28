from pydantic import BaseModel, Field

# البيانات المطلوبة من المستخدِم لتوقع السعر
class PredictionRequest(BaseModel):
    area_sqft: float = Field(..., gt=0, description="المساحة بالقدم المربع")
    bedrooms: int = Field(..., ge=1, description="عدد غرف النوم")
    bathrooms: int = Field(..., ge=1, description="عدد الحمامات")
    balcony: int = Field(..., ge=0, description="عدد البلكونات")
    location: str = Field(..., description="اسم المنطقة")

# الاستجابة اللي السيرفر هيرجعها
class PredictionResponse(BaseModel):
    predicted_price: float = Field(..., description="السعر المتوقع بالعملة INR")