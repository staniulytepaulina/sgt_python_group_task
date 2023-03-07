import sys


def quit():
    print("Goodbye!")
    sys.exit()


def ask_if_wants_to_quit():
    wants_to_quit = str(input("Do you want to quit? Yes/No: ")).lower()
    if wants_to_quit == "yes" or wants_to_quit == "y":
        return True
    elif wants_to_quit == "no" or wants_to_quit == "n":
        return False
    else:
        print("Sorry, I didn't get your answer. Please try again.")
        ask_if_wants_to_quit()
