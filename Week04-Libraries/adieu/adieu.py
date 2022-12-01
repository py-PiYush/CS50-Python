import inflect

p = inflect.engine()

# Get input
names = []
while True:
    try:
        names.append(input().strip())
        my_list = p.join(names)
        print(f"Adieu, adieu, to {my_list}")
    except EOFError:
        break
