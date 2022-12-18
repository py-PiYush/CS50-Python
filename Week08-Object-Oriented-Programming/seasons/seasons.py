import sys
import re
import inflect
from datetime import date


def main():
    # get date in valid format (YYYY-MM-DD)
    user_input = input("Birthday(YYYY-MM-DD): ")
    birthday = get_birthday(user_input)

    # Calculate minutes from birth
    minutes = calculate_minutes(birthday)

    # Print in words
    print(print_words(minutes))


def get_birthday(user_input):
    fmt = r"(\d{4})-(\d{2})-(\d{2})"
    match = re.search(fmt, user_input)
    if not match:
        sys.exit("Invalid")
    year, month, day = map(int, match.groups())
    try:
        birthday = date(year, month, day)
    except ValueError:
        sys.exit()
    return birthday


def calculate_minutes(birthday):
    today = date.today()
    days = (today - birthday).days
    return days * 24 * 60


def print_words(minutes):
    p = inflect.engine()
    word_minute = p.number_to_words(minutes).replace(" and ", " ").capitalize()
    return word_minute + " minutes"


if __name__ == "__main__":
    main()
