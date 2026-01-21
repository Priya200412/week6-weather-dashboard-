from weather_app.weather_display import display_weather

def test_display_weather(capsys):
    current = {
        "city": "Delhi",
        "country": "India",
        "temp": 30,
        "feels_like": 32,
        "humidity": 60,
        "wind": 5,
        "condition": "Clear",
        "time": "2024-02-12 10:00"
    }

    forecast = [
        {"date": "2024-02-13", "max": 32, "min": 25, "condition": "Sunny"}
    ]

    display_weather(current, forecast)

    captured = capsys.readouterr()
    assert "Delhi" in captured.out
    assert "Sunny" in captured.out
