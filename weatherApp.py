# Week 12 - Final Project
# Eric Vargas
# Description: This is a weather program that will ask the user to enter a zip code or city. When this information is
# entered, the current weather data will print. They can also press "x" to quit the program.

import json, requests, re

api_key = "026777141625cba5c967d8478f516c05"
url = "http://api.openweathermap.org/data/2.5/weather?"

print("Welcome to the Weather App!\n")
# Function for Zip Code
def zipCode(zip_code):
    if len(zip_code) != 5: # Checks zip code length (US Zip codes are 5 digits)
        print("ERROR: Please enter a 5 digit Zip Code")
    else:
        try:
            zipURL = url + "appid=" + api_key + "&units=imperial&zip=" + zip_code
            weather_data = requests.get(zipURL).json()

            # prints weather data
            print("\nCurrent weather for " + zip_code +":")
            print('Temperature: {} F'.format(weather_data['main']['temp']))
            print('Description: ' + weather_data['weather'][0]['description'])
            print('Feels Like: {} F'.format(weather_data['main']['feels_like']))
            print('High of: {} F'.format(weather_data['main']['temp_max']))
            print('Low of: {} F'.format(weather_data['main']['temp_min']))

            # checks that request was successful
        except requests.exceptions.RequestException:
            print('Error while fetching data')

# Function for city
def city(city_name):
    try:
        cityURL = url + "appid=" + api_key + "&units=imperial&q=" + city_name
        weather_data = requests.get(cityURL).json()

        # prints weather data
        print("\nCurrent weather for " + city_name +":")
        print('Temperature: {} F'.format(weather_data['main']['temp']))
        print('Description: ' + weather_data['weather'][0]['description'])
        print('Feels Like: {} F'.format(weather_data['main']['feels_like']))
        print('High of: {} F'.format(weather_data['main']['temp_max']))
        print('Low of: {} F'.format(weather_data['main']['temp_min']))

        # checks that request was successful
    except requests.exceptions.RequestException:
        print('Error while fetching data')

# Main function calls either zipCode or City function based on what the user enters.
def main():
    while True:
        user_input = input("\nEnter a Zip Code/City or (x) to Exit: ")
        if user_input.isdigit():

        # prints zip code weather data
            zipCode(user_input)

        # prints city weather data
        elif user_input != "x":
            city(user_input)

        # exits program
        elif user_input == "x":
            print("\nCome back soon!")
            break
main()
