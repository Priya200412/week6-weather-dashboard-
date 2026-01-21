from weather_app.weather_api import WeatherAPI

def test_api_object_creation():
    api = WeatherAPI()
    assert api is not None


def test_get_current_weather_invalid_city():
    api = WeatherAPI()
    result = api.get_current_weather("InvalidCityName123")
    assert result is None or isinstance(result, dict)


def test_get_forecast_invalid_city():
    api = WeatherAPI()
    result = api.get_forecast("InvalidCityName123")
    assert result is None or isinstance(result, dict)
