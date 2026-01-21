from weather_app.weather_api import WeatherAPI
from weather_app.weather_parser import parse_current, parse_forecast
from weather_app.weather_display import display_weather


def main():
    api = WeatherAPI()

    while True:
        city = input("\nSearch city or command (quit): ")

        if city.lower() == "quit":
            print("Goodbye 👋")
            break

        current = api.get_current_weather(city)
        forecast = api.get_forecast(city)

        if current and forecast:
            display_weather(
                parse_current(current),
                parse_forecast(forecast)
            )
        else:
            print("❌ City not found or API error")


if __name__ == "__main__":
    main()
