import random


def main():
    number_of_exp = 10
    score = 0
    level = get_level()
    while number_of_exp:
        first_digit = generate_integer(level)
        second_digit = generate_integer(level)
        result = first_digit + second_digit
        trial = 3
        while trial:
            try:
                user_input = int(input(f"{first_digit} + {second_digit} = ").strip())
                if user_input == result:
                    break
                else:
                    print("EEE")
                    trial -= 1
            except ValueError:
                print("EEE")
                trial -= 1
        if trial == 0:
            print(result)
        else:
            score += 1
        number_of_exp -= 1
    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if not (1 <= level <= 3):
                continue
            return level
        except ValueError:
            pass


def generate_integer(level):
    if not (1 <= level <= 3):
        raise ValueError
    return random.randint((10 ** (level - 1), 0)[level == 1], 10 ** level - 1)


if __name__ == "__main__":
    main()
