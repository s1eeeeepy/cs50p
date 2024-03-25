def main():
    data = get_inp()
    validated = check(data)
    if validated:
        print(f"{data} added")
    else:
        main()


def check(d):
    valid = input("Are you sure you want to add this? (y/n): ")
    if valid == "y":
        return True
    else:
        False


def get_inp():
    data = input(">>> ")
    return data


if __name__ == "__main__":
    main()
