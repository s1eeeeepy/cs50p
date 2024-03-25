import random


while True:
    try:
        level = int(input("Level: "))
        answer = random.randint(1, level)
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess > answer:
        print("Too large!")
        continue
    elif guess < answer:
        print("Too small!")
        continue
    else:
        print("Just right!")
        break
