# Weather Applications

This folder contains two weather forecast applications implemented in Python, catering to both beginner and advanced users. These applications retrieve current weather information for a specified city using the Open Meteo API.

## Beginner-Level Weather App

## Setup

1. **Installation**:
    - Clone this repository to your local machine.
    - Make sure you have Python installed.

2. **Dependencies**:
    - This script requires the following Python libraries:
        - `requests`
        - `geopy`
        - `prettytable`

    You can install these dependencies using pip:
    ```
    pip install requests geopy prettytable
    ```

3. **API Key**:
    - This script uses the Open Meteo API to fetch weather forecast data. You need to sign up for an API key [here](https://open-meteo.com/signup) and The Open Meteo API is publicly accessible, allowing users to make requests to the API endpoint without any authentication.. 
## Usage

1. **Run the Script**:
    - Open a terminal or command prompt.
    - Navigate to the directory containing the script.
    - Run the script using Python:
    ```
    python weather_app_beginner.py
    ```

2. **Enter City Name**:
    - You will be prompted to enter the name of the city for which you want to retrieve the weather forecast.

3. **View Weather Forecast**:
    - The script will display the current weather information for the specified city, including temperature, humidity, surface pressure, and wind speed.

## Advanced-Level Weather App

## Features

- **User Input**: Enter the name of the city for which you want to retrieve the weather forecast.
- **Display Weather**: Upon clicking the "Get Weather" button, the application fetches weather data and displays it.
- **Weather Information**: Shows various weather parameters including temperature, humidity, precipitation, wind speed, etc.

## Setup

1. **Dependencies**:
    - Ensure you have Python installed on your system.
    - Install required Python libraries:
        ```
        pip install tkinter requests geopy pillow
        ```

2. **API Key**:
    - This application uses the Open Meteo API to fetch weather forecast data. You need to sign up for an API key [here](https://open-meteo.com/signup) and The Open Meteo API is publicly accessible, allowing users to make requests to the API endpoint without any authentication..

## Usage

1. **Run the Application**:
    - Execute the Python script `weather_app_advanced.py`.
    ```
    python weather_app_advanced.py
    ```

2. **Enter City Name**:
    - In the GUI window that appears, enter the name of the city for which you want to retrieve the weather forecast.

3. **Get Weather**:
    - Click the "Get Weather" button.
    - The application will display the current weather information for the specified city.

## Credits

- This application uses the [Open Meteo API](https://open-meteo.com) to fetch weather data.
- Developed by [Demiso Daba](https://github.com/DemisoDaba).

## License

This project is licensed under the [MIT License](LICENSE).

