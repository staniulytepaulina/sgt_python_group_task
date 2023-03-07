Def deposit(self):
    amount=float(input("Enter amount to be Deposited: "))
    self.balance += amount
    print("\n Amount Deposited:",amount)
