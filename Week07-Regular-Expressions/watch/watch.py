import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/(.+?)"'
    match = re.search(pattern, s)
    if match:
        link = match.group(1)
        return f"https://youtu.be/{link}"


if __name__ == "__main__":
    main()
