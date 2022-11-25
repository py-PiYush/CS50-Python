def main():
    # take and split user input
    x, y, z = input("Enter expression: ").strip().split(" ")

    # Based on operator, perform operation
    if y == "+":
        print(add(float(x), float(z)))

    elif y == "-":
        print(subtract(float(x), float(z)))

    elif y == "*":
        print(multiply(float(x), float(z)))

    else:
        print(divide(float(x), float(z)))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


main()
