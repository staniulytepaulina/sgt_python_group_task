import constants


def withdraw():
    withdraw_amt = float(input("Enter the amount to withdraw: "))
    if withdraw_amt > constants.BALANCE:
        print("Can't withdraw", withdraw_amt, "because you don't have enough money")
        print("Try with lower amount than balance")
    else:
        print(f"You have withdrawn {withdraw_amt} from your account,you remaining balance is", (constants.BALANCE - withdraw_amt))
        return constants.BALANCE - withdraw_amt
