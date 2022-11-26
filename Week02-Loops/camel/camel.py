text = input("Enter camelCase: ").strip()
for ch in text:
    if ch.isupper():
        print(f"_{ch.lower()}", end="")
    else:
        print(ch, end="")
print()
