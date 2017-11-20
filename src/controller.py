import os
import api
import zips
import views


def generate_report():

    zip_code = get_zip()
    zip_list = zips.get_zips()

    if zip_code in zip_list:
        weather_dict = api.get_weather(zip_code) 
        print(views.weather_report(weather_dict))
    else:
        next_move = input("Sorry. we don't recognize that Zip. Please Try again >> ")



def get_zip():
    zip_code = input("Please enter your zip-code >> ") 
    return int(zip_code)


def generate_help_menu()