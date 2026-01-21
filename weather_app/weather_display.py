def display_weather(current, forecast):
    print("\n🌤️ WEATHER DASHBOARD")
    print("=" * 40)

    print(f"\n📍 {current['city']}, {current['country']}")
    print(f"🕒 Time: {current['time']}")
    print(f"🌡️ Temp: {current['temp']}°C (Feels {current['feels_like']}°C)")
    print(f"💧 Humidity: {current['humidity']}%")
    print(f"🌬️ Wind: {current['wind']} km/h")
    print(f"🌥️ Condition: {current['condition']}")

    print("\n5-Day Forecast")
    print("-" * 40)
    for day in forecast:
        print(f"{day['date']} → {day['condition']} | {day['max']}°C / {day['min']}°C")
