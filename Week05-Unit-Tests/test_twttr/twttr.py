def main():
    text = input("Input: ").strip()
    shortened = shorten(text)
    print(shortened)


def shorten(word):
    res = ""
    for ch in word:
        if ch in "aeiouAEIOU":
            continue
        res += ch
    return res


if __name__ == "__main__":
    main()
