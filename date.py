from datetime import date, datetime
import inflect
import re
import sys


def main():
    text = convert(subtract(get_date())).capitalize()
    out = del_and(text)
    print(f"{out} minutes")


def get_date():
    birth = input("Date of Birth: ")
    if matches := re.search(r"^(\d\d\d\d)-(\d\d)-(\d\d)$", birth):
        if 1 <= int(matches.group(2)) <= 12 and 1 <= int(matches.group(3)) <= 31:
            return date(
                int(matches.group(1)), int(matches.group(2)), int(matches.group(3))
            )
        else:
            sys.exit("Invalid date")
    else:
        sys.exit("Inbalid date")


def subtract(d):
    days = (date.today() - d).days
    return days * 24 * 60


def convert(n):
    p = inflect.engine()
    return p.number_to_words(n)


def del_and(text):
    if matches := re.findall(r"\Wand\W", text, re.IGNORECASE):
        for match in matches:
            text = text.replace(match, " ")
    return text


if __name__ == "__main__":
    main()
