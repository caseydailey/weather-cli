import os
import controller

"""
    This module provides a relay between the user and the controller
"""

def main():

    os.system('clear')
    print(views.main_menu())

    choice = input(">> ")

    if choice == '1':
        controller.generate_report()

    if choice == '2':
        controller.generate_help_menu()

    if choice =='3':
        quit()

    main()



if __name__ == '__main__':
    main()
