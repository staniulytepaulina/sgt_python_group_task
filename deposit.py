import constants


def deposit():
    amount = float(input("Enter amount to be Deposited: "))
    constants.BALANCE += amount
    print("\n Amount Deposited:", amount)
