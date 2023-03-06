def deposit(amount):
    global CURRENT_BALANCE
    CURRENT_BALANCE += amount
    return CURRENT_BALANCE
