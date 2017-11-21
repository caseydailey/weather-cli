import os
import api
import zips
import views
import main


"""
    This module flips the switches between the menu and the other helper modules
"""

def generate_report():

    zip_code = get_zip()
    zip_list = zips.get_zips()

    if zip_code in zip_list:
        weather_dict = api.get_weather(zip_code) 
        print(views.weather_report(weather_dict))
        next_move = input("press enter to return the main menu > ")
        if next_move:
            return            
    else:
        print("Sorry. we don't recognize that Zip.")
        generate_report()




def get_zip():
    zip_code = input("Please enter your zip-code >> ") 
    return int(zip_code)


