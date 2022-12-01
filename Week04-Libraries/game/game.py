import random


def get_positive_int(prompt):
    while True:
        try:
            level = int(input(f"{prompt}: ").strip())
            if level <= 0:
                continue
            # print(level)
            return level
        except ValueError:
            pass


level = get_positive_int("Level")
r = random.randint(1, level)
while True:
    guessed = get_positive_int("Guess")
    if r == guessed:
        print("Just Right!")
        break
    elif r > guessed:
        print("Too small!")
    else:
        print("Too large!")
