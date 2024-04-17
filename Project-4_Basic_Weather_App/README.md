# Weather Forecast Applications

This folder contains two weather forecast applications implemented in Python, catering to both beginner and advanced users. These applications retrieve current weather information for a specified city using the Open Meteo API.

## Beginner-Level Weather App

### Features

- **User-Friendly Interface**: Utilizes Tkinter for a simple GUI.
- **Basic Weather Display**: Shows essential weather parameters such as temperature, humidity, and precipitation.

## Advanced-Level Weather App

### Features

- **Advanced GUI**: Employs Tkinter for a more sophisticated user interface.
- **Comprehensive Weather Data**: Displays a wide range of weather parameters including wind speed, cloud cover, and surface pressure.
- **Error Handling**: Provides error messages for failed API requests and invalid city names.

## Setup and Usage

1. **Clone the Repository**:
    ```
    git clone <repository_url>
    cd weather-forecast
    ```

2. **Install Dependencies**:
    ```
    pip install -r requirements.txt
    ```

3. **API Key**:
    - Sign up for an API key [here](https://open-meteo.com/signup).
    - Replace `<YOUR_API_KEY>` in the code with your actual API key.

4. **Run the Applications**:
    - For the Beginner-Level Weather App:
        ```
        python beginner_weather_app.py
        ```
    - For the Advanced-Level Weather App:
        ```
        python advanced_weather_app.py
        ```

5. **Enter City Name**:
    - In the GUI window that appears, enter the name of the city for which you want to retrieve the weather forecast.

6. **Get Weather**:
    - Click the "Get Weather" button.
    - The application will display the current weather information for the specified city.

## Credits

- This application uses the [Open Meteo API](https://open-meteo.com) to fetch weather data.
- Developed by [Your Name].

## License

This project is licensed under the [MIT License](LICENSE).

