balance = 1000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient balance")

deposit(500)
withdraw(200)
deposit(300)
withdraw(2000)

print("Final balance:", balance)