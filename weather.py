
import requests
API_KEY="PUT_OPENWEATHER_KEY"

def get_weather(city):
    if API_KEY.startswith("PUT"):
        return "Weather API not configured."
    r=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric").json()
    return f"{city}: {r['main']['temp']}°C, {r['weather'][0]['description']}"
