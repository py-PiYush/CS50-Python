def main():
    x, y = get_fraction()
    print_res(x, y)


def get_fraction():
    while True:
        try:
            a, b = input("Fraction: ").strip().split("/")
            int_a, int_b = int(a), int(b)
            if int_a > int_b:
                continue
            return int_a, int_b
        except ValueError:
            pass


def print_res(a, b):
    try:
        perc = round(a * 100 / b)
        if perc <= 1:
            print("E")
        elif perc >= 99:
            print("F")
        else:
            print(f"{perc}%")
    except ZeroDivisionError:
        main()


main()
