import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from geopy.geocoders import Nominatim

def fetch_forecast(latitude, longitude):
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m")
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching weather forecast data: {e}")
        return None

def get_coordinates(city_name):
    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city_name)
        if location:
            return location.latitude, location.longitude
        else:
            print("Location not found.")
            return None, None
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def display_weather(location):
    # Fetch weather data
    forecast_data = fetch_forecast(location.latitude, location.longitude)
    if forecast_data:
        current_weather = forecast_data['current']
        print("Weather data retrieved successfully:")
        print(current_weather)

        # Extract specific weather information
        time = current_weather['time']
        temperature = current_weather['temperature_2m']
        humidity = current_weather['relative_humidity_2m']
        apparent_temperature = current_weather['apparent_temperature']
        precipitation = current_weather['precipitation']
        rain = current_weather['rain']
        showers = current_weather['showers']
        snowfall = current_weather['snowfall']
        weather_code = current_weather['weather_code']
        cloud_cover = current_weather['cloud_cover']
        pressure_msl = current_weather['pressure_msl']
        surface_pressure = current_weather['surface_pressure']
        wind_speed = current_weather['wind_speed_10m']
        wind_direction = current_weather['wind_direction_10m']
        wind_gusts = current_weather['wind_gusts_10m']

        # Update the GUI with weather information
        weather_info_label.config(text=f"Time: {time}\n"
                                        f"Temperature (°C): {temperature}\n"
                                        f"Relative Humidity (%): {humidity}\n"
                                        f"Apparent Temperature (°C): {apparent_temperature}\n"
                                        f"Precipitation: {precipitation}\n"
                                        f"Rain: {rain}\n"
                                        f"Showers: {showers}\n"
                                        f"Snowfall: {snowfall}\n"
                                        f"Weather Code: {weather_code}\n"
                                        f"Cloud Cover (%): {cloud_cover}\n"
                                        f"MSL Pressure (hPa): {pressure_msl}\n"
                                        f"Surface Pressure (hPa): {surface_pressure}\n"
                                        f"Wind Speed (m/s): {wind_speed}\n"
                                        f"Wind Direction (°): {wind_direction}\n"
                                        f"Wind Gusts (m/s): {wind_gusts}")
        info_label.config(text="This is full info" , font=("Helvetica", 14))
    else:
        print("Failed to fetch weather data.")

def get_weather():
    city_name = entry.get()
    latitude, longitude = get_coordinates(city_name)
    if latitude is not None and longitude is not None:
        location = type('', (), {})()  # Creating a simple class object to store latitude and longitude
        location.latitude = latitude
        location.longitude = longitude
        display_weather(location)
    else:
        messagebox.showerror("Error", "Failed to retrieve coordinates for the specified city.")

# GUI setup
root = tk.Tk()
root.title("Current Weather App")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Enter city name:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

button = tk.Button(frame, text="Get Weather", command=get_weather)
button.grid(row=0, column=2)

weather_info_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
weather_info_frame.pack(padx=10, pady=10)

info_label = tk.Label(weather_info_frame, text="")
info_label.pack()

weather_info_label = tk.Label(weather_info_frame, text="")
weather_info_label.pack()

root.mainloop()
