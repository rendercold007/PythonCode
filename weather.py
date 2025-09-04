import requests
import json
from datetime import datetime

API_KEY = "4f650b2e5f61f4951f351f7ac3195789"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)   # requests.get() makes HTTP request (like browser visiting URL)
        response.raise_for_status()   #params adds ?key=value to URL automatically
        return response.json()
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            print(f" City '{city_name}' not found!")
        else:
            print(f" HTTP Error: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f" Error: {err}")
        return None
    

def display_weather(data):
    if not data:
        return

    city = data['name']
    country = data['sys']['country']    
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    weather = data['weather'][0]['description']
    wind_speed = data['wind']['speed']


    print("\n" + "=" * 45)
    print(f" Weather in {city}, {country}")
    print("=" * 49)
    print(f" Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"  Condition: {weather.capitalize()}")
    print(f" Humidity: {humidity}%")
    print(f" Wind Speed: {wind_speed} m/s")
    print(f" Pressure: {pressure} hPa")
    print("="*50)

def main():
    print(" WEATHER APP")
    print("-" * 30)

    while True:
        city = input("\n Enter city name (or 'quit' to exit): ").strip()

        if city.lower() == 'quit':
            print("Thanks for using Weather APP! Goodbye! ")
            break

        if city:
            print(f" \nFetching weather for {city}...")
            weather_data = get_weather(city)
            display_weather(weather_data)
        else:
            print("Please enter a vaid city name!")


if __name__ == "__main__":
    main()            