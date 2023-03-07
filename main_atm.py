import language
import balance
import deposit
import withdraw
import password
from quit import quit, ask_if_wants_to_quit

chosen_option = 0


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
            balance.balance()
            ask_if_wants_to_do_another_action()
        case 2:
            deposit.deposit()
            balance.balance()
            ask_if_wants_to_do_another_action()
        case 3:
            withdraw.withdraw()
            ask_if_wants_to_do_another_action()
        case 4:
            quit()


def ask_if_wants_to_do_another_action():
    needs_another_action = ask_if_wants_to_quit()
    if needs_another_action:
        quit()
    else:
        atm_options()


def atm():
    language.choose_language()
    is_pin_correct = password.check_pin()
    if is_pin_correct:
        atm_options()


def atm_options():
    show_menu()
    check_if_option_is_valid(choose_menu_option())


atm()
