from datetime import datetime

def parse_current(data):
    return {
        "city": data["location"]["name"],
        "country": data["location"]["country"],
        "temp": data["current"]["temp_c"],
        "feels_like": data["current"]["feelslike_c"],
        "humidity": data["current"]["humidity"],
        "pressure": data["current"]["pressure_mb"],
        "wind": data["current"]["wind_kph"],
        "condition": data["current"]["condition"]["text"],
        "time": data["location"]["localtime"]
    }


def parse_forecast(data):
    forecast = []
    for day in data["forecast"]["forecastday"]:
        forecast.append({
            "date": day["date"],
            "max": day["day"]["maxtemp_c"],
            "min": day["day"]["mintemp_c"],
            "condition": day["day"]["condition"]["text"]
        })
    return forecast
