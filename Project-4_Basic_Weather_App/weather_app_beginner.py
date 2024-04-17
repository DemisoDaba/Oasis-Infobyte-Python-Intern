import requests
from geopy.geocoders import Nominatim
from prettytable import PrettyTable

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

def main():
    city_name = input("Enter city name: ")
    latitude, longitude = get_coordinates(city_name)
    if latitude is not None and longitude is not None:
        forecast_data = fetch_forecast(latitude, longitude)
        if forecast_data:
            current_weather = forecast_data['current']
            table = PrettyTable()
            table.field_names = [
                "Attribute", "Value"
            ]
            table.add_row(["Time", current_weather['time']])
            table.add_row(["Temperature (°C)", current_weather['temperature_2m']])
            table.add_row(["Relative Humidity (%)", current_weather['relative_humidity_2m']])
            table.add_row(["Surface Pressure (hPa)", current_weather['surface_pressure']])
            table.add_row(["Wind Speed (m/s)", current_weather['wind_speed_10m']])
            print(table)
        else:
            print("Failed to fetch weather forecast data.")
    else:
        print("Failed to retrieve coordinates for the specified city.")

if __name__ == "__main__":
    main()
