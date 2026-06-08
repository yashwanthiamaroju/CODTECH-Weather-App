weather_data = {
    "Hyderabad": "32°C, Sunny",
    "Delhi": "38°C, Hot",
    "Mumbai": "29°C, Cloudy",
    "Chennai": "34°C, Humid"
}

city = input("Enter city name: ")

if city in weather_data:
    print("Weather in", city + ":", weather_data[city])
else:
    print("City not found!")