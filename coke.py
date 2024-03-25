coins = [25, 10, 5]
price = 50
while price > 0:
    amount = int(input("Insert Coin: "))
    if amount in coins:
        price -= amount
        if price > 0:
            print(f"Amount Due: {price}")
    else:
        print(f"Amount Due: {price}")
        continue
print(f"Change owed: {abs(price)}")
