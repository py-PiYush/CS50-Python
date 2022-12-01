def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    # strip off surrounding white spaces and make it case-insensitive
    greet = greeting.strip().lower()

    # $0 if greeting is hello
    if greet.startswith("hello"):
        return 0

    # $20 if greeting starts with 'h'
    elif greet.startswith("h"):
        return 20

    # $100 otherwise
    else:
        return 100


if __name__ == "__main__":
    main()
