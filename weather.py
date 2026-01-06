import os
import requests

API_KEY = os.environ.get("OPENWEATHER_API_KEY")

def get_weather(city):
    # If no API key is set, return safe message
    if not API_KEY:
        return {
            "city": city,
            "temperature": "N/A",
            "condition": "Weather service not configured"
        }

    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        # Handle API errors safely
        if response.status_code != 200:
            return {
                "city": city,
                "temperature": "N/A",
                "condition": "City not found or API error"
            }

        return {
            "city": city,
            "temperature": f"{data['main']['temp']} °C",
            "condition": data["weather"][0]["description"]
        }

    except Exception as e:
        return {
            "city": city,
            "temperature": "N/A",
            "condition": "Weather service unavailable"
        }
