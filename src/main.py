import os
import api
import zips
import views
import controller

def main():

    clear()
    print(views.main_menu())

    choice = input(">> ")

    if choice == '1':
        controller.generate_report()

    if choice == '2':
        controller.generate_help_menu()

    if choice =='3':
        quit()
        
    main()

def clear():
    os.system('clear')

if __name__ == '__main__':
    main()
