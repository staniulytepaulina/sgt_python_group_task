current_balance = 100
withdraw_amount = int(input("Enter the amount to withdraw: "))
def withdraw(withdraw_amt):
    if withdraw_amt > current_balance:
        print("Can't withdraw", withdraw_amt, "because you don't have enough money")
        print("Try with lower amount than balance")
    else:
        print(f"You have withdrawn {withdraw_amount} from your account,you remaining balance is", (current_balance-withdraw_amount))
        return current_balance-withdraw_amount