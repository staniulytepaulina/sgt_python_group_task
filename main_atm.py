import sys
import constants
import language
import balance
import deposit
import withdraw
import password
from quit import quit, ask_if_wants_to_quit

chosen_option = 0
pin_tries = 3


def show_menu():
    print("Choose 1 to check balance.")
    print("Choose 2 to deposit money.")
    print("Choose 3 to withdraw money.")
    print("Choose 4 to quit.")


def choose_menu_option():
    return int(input("Please choose your option: "))


def check_if_option_is_valid(option):
    if option <= 0 or option > 4:
        print("There is no such option, please choose again.")
        atm_options()
    else:
        call_based_option(option)


def call_based_option(option):
    match option:
        case 1:
            print("balance")
            #
            ask_if_wants_to_do_another_action()
        case 2:
            print("deposit")
            #
            ask_if_wants_to_do_another_action()
        case 3:
            print("withdraw")
            #
            ask_if_wants_to_do_another_action()
        case 4:
            quit()


def ask_if_wants_to_do_another_action():
    needs_another_action = ask_if_wants_to_quit()
    if needs_another_action:
        quit()
    else:
        atm_options()


def check_password():
    global pin_tries
    pin = str(input("Input your pin number: "))
    if pin == constants.password:
        choose_language()
    else:
        if pin_tries > 1:
            pin_tries = pin_tries - 1
            print(f"Pin incorrect. You have remaining {pin_tries} tries. Try again:")
            check_password()
        else:
            print("You have been locked out of your account.")
            sys.exit()


def choose_language():
    language = input(f"Please choose a language ({constants.languages}): ")
    if language.capitalize() in constants.languages:
        print(f"You've selected {language} language.")
        return language.capitalize()
    else:
        print(f"We didn't understand you. We will keep English language for you.")
        return "English"


def atm():
    check_password()
    atm_options()


def atm_options():
    show_menu()
    check_if_option_is_valid(choose_menu_option())


atm()
