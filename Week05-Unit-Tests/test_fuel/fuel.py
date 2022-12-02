def main():
    fraction = input("Fraction: ").strip()
    percentage = convert(fraction)
    result = gauge(percentage)
    print(result)


def convert(fraction):
    while True:
        try:
            a, b = fraction.split("/")
            int_a, int_b = int(a), int(b)
            if int_a > int_b:
                continue
        except ValueError:
            raise
        else:
            try:
                perc = round(int_a * 100 / int_b)
            except ZeroDivisionError:
                raise
            else:
                return perc


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
