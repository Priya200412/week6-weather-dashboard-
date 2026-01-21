import requests
import json
import time
from pathlib import Path
from weather_app.config import API_KEY, BASE_URL, CACHE_DURATION


class WeatherAPI:
    def __init__(self):
        self.cache_dir = Path("data/cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _cache_file(self, key):
        return self.cache_dir / f"{key}.json"

    def _get_cache(self, key):
        file = self._cache_file(key)
        if file.exists() and time.time() - file.stat().st_mtime < CACHE_DURATION:
            with open(file) as f:
                return json.load(f)
        return None

    def _save_cache(self, key, data):
        with open(self._cache_file(key), "w") as f:
            json.dump(data, f, indent=2)

    def get_current_weather(self, city):
        key = f"current_{city.lower()}"
        cached = self._get_cache(key)
        if cached:
            return cached

        url = f"https://api.weatherapi.com/v1/current.json?key=226b793138e341c7b95155050262101&q={city},IN"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self._save_cache(key, data)
            return data
        else:
            return None

    def get_forecast(self, city):
        url = f"https://api.weatherapi.com/v1/forecast.json?key=226b793138e341c7b95155050262101&q={city}&days=5"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
