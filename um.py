import re
import sys


def main():
    print(count(input("Text: ").lower()))


def count(s):
    matches = re.findall(r"\W?um\W*", s)
    count = 0
    words = s.split(" ")
    for u in matches:
        if u.strip() in words:
            count += 1
    return count


if __name__ == "__main__":
    main()
