balance = 0


def main():
    print(balance)
    deposit(100)
    withdraw(50)
    print(balance)


def deposit(amount):
    global balance
    balance += amount


def withdraw(amount):
    global balance
    balance -= amount


if __name__ == "__main__":
    main()
