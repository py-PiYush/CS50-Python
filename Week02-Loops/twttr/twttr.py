text = input("Input: ").strip()
for ch in text:
    if ch in "aeiouAEIOU":
        continue
    print(ch, end="")
print()
