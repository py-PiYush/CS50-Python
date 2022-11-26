months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ").strip()

    # Case 1
    if "/" in date:
        m, d, y = date.split("/")
        try:
            m, d, y = int(m), int(d), int(y)
            # Check for valid month, day, year
            if not (1 <= m <= 12 and 1 <= d <= 31 and y > 999):
                continue
            print(f"{y:04}-{m:02}-{d:02}")
            break

        except ValueError:
            pass

    # Case 2:
    elif ", " in date:
        date = date.replace(", ", " ")
        m, d, y = date.split(" ")
        try:
            m, d, y = months.index(m.capitalize()) + 1, int(d), int(y)
            # Check for valid month, day, year
            if not (1 <= m <= 12 and 1 <= d <= 31 and y > 999):
                continue
            print(f"{y:04}-{m:02}-{d:02}")
            break
        except ValueError or KeyError:
            pass

    else:
        continue
