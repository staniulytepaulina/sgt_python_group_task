import sys


def quit():
    print("Goodbye!")
    sys.exit()


def ask_if_wants_to_quit():
    needs_another_action = str(input("Do you want to quit? Yes/No: ")).lower()
    if needs_another_action == "yes" or needs_another_action == "y":
        return True
    elif needs_another_action == "no" or needs_another_action == "n":
        return False
    else:
        print("Sorry, I didn't get your answer. Please try again.")
        ask_if_wants_to_quit()
