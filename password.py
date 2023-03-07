correct_pin = 1234

def check_pin(correct_pin):
    tries = 3
    while tries >= 0:
        input_pin = int(input("Enter your pin: \n"))
        if input_pin == correct_pin:
            print("Account authorized!")
            return True
        else:
            tries += -1
            print("PIN incorrect! Number of tries left: ", tries, end = "\n\n")
            if tries == 0:
                print("I am LOCKIN' you out now!")
                return False
