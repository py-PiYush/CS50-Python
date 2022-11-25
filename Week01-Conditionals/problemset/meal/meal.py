def main():
    # Take user input
    time = input("Enter Meal Time: ").strip()

    # Convert to number of hours
    hours = convert(time)

    # Based on hours, print breakfast, lunch, dinner (if-else block)
    if 7 <= hours <= 8:
        print("breakfast time")

    elif 12 <= hours <= 13:
        print("lunch time")

    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    hour, minutes = time.split(":")
    return int(hour) + int(minutes) / 60


if __name__ == "__main__":
    main()
