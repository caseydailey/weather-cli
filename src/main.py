import os
import api
import zips
import views

def main():

    os.system('clear')
    print(views.main_menu())
    choice = input(">> ")
    while choice != "3":
        if choice == "1":
            print(zips.get_zips())
            zip_code = input("Please enter your zip-code >> ")
            if zip_code in zips.get_zips():
                weather = api.get_weather(zip_code) 
                print(views.weather_report(weather))
            else:
                zip_code = input("Sorry. we don't recognize that Zip")




if __name__ == '__main__':
    main()
