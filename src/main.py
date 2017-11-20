import os
import api
import zips
import views
import controller

def main():

    clear()
    print(views.main_menu())

    choice = input(">> ")

    while choice != '3':

        if choice == '1':
            controller.generate_report()

        elif choice == '2':
            controller.generate_help_menu()

        else:
            controller.say_bye()

def clear():
    os.system('clear')

if __name__ == '__main__':
    main()
