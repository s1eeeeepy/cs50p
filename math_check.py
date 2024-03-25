import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        mst = 0
        while mst < 3:
            exp = f"{x} + {y}"
            try:
                guess = int(input(f"{exp} = "))
                if guess == eval(exp):
                    score += 1
                    break
                else:
                    print("EEE")
                    mst += 1
            except ValueError:
                print("EEE")
                mst += 1
        if mst == 3:
            print(exp, "=", eval(exp))
    print(score)


def get_level():
    while True:
        try:
            levels = [1, 2, 3]
            level = input("Level: ")
            if int(level) in levels:
                return int(level)
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
    return x


if __name__ == "__main__":
    main()
