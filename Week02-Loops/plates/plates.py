def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check for number of characters
    size = len(s)
    if not 2 <= size <= 6:
        return False

    # Check for start
    if not s[:2].isalpha():
        return False

    # Check for first number is not zero
    number = False
    for ch in s:
        if ch.isdigit():
            if not number and ch == "0":
                return False
            number = True

        # Check for alphabet after number
        elif number and ch.isalpha():
            return False

    # check for punctuation, spaces, periods
    if not s.isalnum():
        return False

    return True


main()
