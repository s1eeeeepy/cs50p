import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    links = ["http://youtube.com", "https://youtube.com", "https://www.youtube.com"]
    if matches := re.search(r'^(?:.*)?src="(.+)/.*/(\w+)".*$', s):
        if matches.group(1) in links:
            return f"https://youtu.be/{matches.group(2)}"
        else:
            return None


if __name__ == "__main__":
    main()
