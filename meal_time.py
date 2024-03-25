def main():
    dt = convert(input("What time is it? "))
    if 7 <= dt <= 8:
        print("breakfast time")
    elif 12 <= dt <= 13:
        print("lunch time")
    elif 18 <= dt <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    splited = time.split(":")
    dec = int(splited[-1]) / 60
    dt = float(splited[0]) + dec
    return dt


if __name__ == "__main__":
    main()
