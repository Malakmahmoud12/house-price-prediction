from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "House Price Prediction API"
    
    # تحديد المسارات الأساسية
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent.parent
    MODEL_PATH: Path = BASE_DIR / "models" / "house_price.pkl"
    LOCATIONS_PATH: Path = BASE_DIR / "models" / "locations.json"

    class Config:
        case_sensitive = True

settings = Settings()