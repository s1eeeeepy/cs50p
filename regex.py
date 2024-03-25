import re


while True:
    url = input("URL: ").strip()
    if matches := re.search(
        r"^(?:.*)?twitter\.com/(\w+).*$",
        url,
        re.IGNORECASE,
    ):
        username = matches.group(1)
        break
    else:
        print("Invalid URL, please try again")

print(f"Username: {username}")
