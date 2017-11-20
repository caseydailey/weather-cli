import os
import api
import zips
import controller
import views

def main():

    os.system('clear')
    print(views.main_menu())
    choice = input(">> ")
    while choice != 3:
        if choice == 1:
            zip_code = input("Please enter your zip-code >> ")
            if zip_code in zips.get_zips:
                weather = controller.get_weather(zip_code) 
                print(views.weather_report(weather))
            else:
                zip_code = input("Sorry. we don't recognize that Zip")




if __name__ == '__main__':
    main()
