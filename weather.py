import requests
import os

API_KEY = os.environ.get("OPENWEATHER_API_KEY")

def get_weather(city):
    if not API_KEY:
        return "Weather service not configured."

    try:
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            },
            timeout=5
        )
        data = r.json()

        if r.status_code != 200:
            return "Weather data unavailable."

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"{city}: {temp}°C, {desc}"

    except Exception:
        return "Weather service error."
