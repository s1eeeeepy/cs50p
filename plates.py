def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    approved = 0
    if s[:2].isalpha():
        approved += 1
    if 2 <= len(s) <= 6:
        approved += 1
    for e in s:
        if e in "'.,;:?! ":
            return False
    for n in range(len(s) - 1):
        if s[n].isdigit() and s[n + 1].isalpha():
            return False
    for n in range(len(s) - 1):
        if s[n].isalpha() and s[n + 1] == "0":
            return False
    if approved == 2:
        return True


if __name__ == "__main__":
    main()
