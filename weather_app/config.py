import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    raise ValueError("WEATHER_API_KEY not found in .env file")
BASE_URL = "https://api.weatherapi.com/v1"
CACHE_DURATION = 600
