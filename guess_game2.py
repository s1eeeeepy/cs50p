import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            continue


def main(level):
    answer = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        if guess > 0:
            if guess > answer:
                print("Too large!")
                continue
            elif guess < answer:
                print("Too small!")
                continue
            else:
                print("Just right!")
                break
        else:
            continue


if __name__ == "__main__":
    main(get_level())
