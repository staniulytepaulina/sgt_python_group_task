import constants


def check_pin():
    while constants.PIN_TRIES > 0:
        input_pin = int(input("Enter your pin: \n"))
        if input_pin == constants.CORRECT_PIN:
            print("Account authorized!")
            return True
        else:
            constants.PIN_TRIES -= 1
            print("PIN incorrect! Number of tries left: ", constants.PIN_TRIES, end = "\n\n")
            if constants.PIN_TRIES == 0:
                print("I am LOCKIN' you out now!")
                return False
