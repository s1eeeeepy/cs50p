import re
import sys
from validator_collection import validators


def main():
    print(validate(input("Email: ").strip()))


def validate(s):
    if validators.email(s):
        return True
    else:
        sys.exit()


if __name__ == "__main__":
    main()
