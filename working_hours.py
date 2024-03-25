import re
import sys


am = {
    "1": "01:00",
    "2": "02:00",
    "3": "03:00",
    "4": "04:00",
    "5": "05:00",
    "6": "06:00",
    "7": "07:00",
    "8": "08:00",
    "9": "09:00",
    "10": "10:00",
    "11": "11:00",
    "12": "00:00",
}
pm = {
    "1": "13:00",
    "2": "14:00",
    "3": "15:00",
    "4": "16:00",
    "5": "17:00",
    "6": "18:00",
    "7": "19:00",
    "8": "20:00",
    "9": "21:00",
    "10": "22:00",
    "11": "23:00",
    "12": "12:00",
}


def main():
    print(str(convert(input("Hours: "))))


def convert(s):
    if matches := re.search(r"^(\d+)(?::00)? (AM|PM) to (\d+)(?::00)? (AM|PM)$", s):
        if matches.group(4) == "PM" and matches.group(2) == "AM":
            return f"{am[matches.group(1)]} to {pm[matches.group(3)]}"
        if matches.group(2) == "PM" and matches.group(4) == "AM":
            return f"{pm[matches.group(1)]} to {am[matches.group(3)]}"
    raise ValueError


if __name__ == "__main__":
    main()
