import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2}):?(\d\d)? (AM|PM) to (\d{1,2}):?(\d\d)? (AM|PM)$"
    match = re.search(pattern, s)
    if match is None:
        raise ValueError
    hr1, mn1, mer1, hr2, mn2, mer2 = match.groups()
    if mn1 is not None and mn2 is not None:
        time_24 = minute_fmt(hr1, mn1, mer1, hr2, mn2, mer2)
    elif mn1 is not None or mn2 is not None:
        raise ValueError
    else:
        time_24 = no_fmt(hr1, mer1, hr2, mer2)

    return time_24


def minute_fmt(hr1, mn1, mer1, hr2, mn2, mer2):
    """e.g. 9:00 AM to 5:00 PM"""
    hr1, mn1, hr2, mn2 = int(hr1), int(mn1), int(hr2), int(mn2)
    if not (0 < hr1 <= 12 and 0 <= mn1 < 60 and 0 < hr2 <= 12 and 0 <= mn2 < 60):
        raise ValueError
    if mer1 == "AM" and hr1 == 12:
        hr1 = 0
    if mer2 == "AM" and hr2 == 12:
        hr2 = 0
    if mer1 == "PM" and hr1 != 12:
        hr1 = hr1 + 12
    if mer2 == "PM" and hr2 != 12:
        hr2 = hr2 + 12
    return f"{hr1:02d}:{mn1:02d} to {hr2:02d}:{mn2:02d}"


def no_fmt(hr1, mer1, hr2, mer2):
    hr1, hr2 = int(hr1), int(hr2)
    if not (0 < hr1 <= 12 and 0 < hr2 <= 12):
        raise ValueError
    if mer1 == "AM" and hr1 == 12:
        hr1 = 0
    if mer2 == "AM" and hr2 == 12:
        hr2 = 0
    if mer1 == "PM" and hr1 != 12:
        hr1 = hr1 + 12
    if mer2 == "PM" and hr2 != 12:
        hr2 = hr2 + 12
    return f"{hr1:02d}:00 to {hr2:02d}:00"


if __name__ == "__main__":
    main()
