from weather_app.weather_parser import parse_current, parse_forecast

def test_parse_current():
    sample_data = {
        "location": {"name": "Delhi", "country": "India"},
        "current": {
            "temp_c": 30,
            "feelslike_c": 32,
            "humidity": 60,
            "pressure_mb": 1012,
            "wind_kph": 5,
            "condition": {"text": "Clear"},
        }
    }

    result = parse_current(sample_data)

    assert result["city"] == "Delhi"
    assert result["country"] == "India"
    assert result["temp"] == 30
    assert result["humidity"] == 60


def test_parse_forecast():
    sample_data = {
        "forecast": {
            "forecastday": [
                {
                    "date": "2024-02-12",
                    "day": {
                        "maxtemp_c": 32,
                        "mintemp_c": 25,
                        "condition": {"text": "Sunny"}
                    }
                }
            ]
        }
    }

    result = parse_forecast(sample_data)
    assert len(result) == 1
    assert result[0]["condition"] == "Sunny"
