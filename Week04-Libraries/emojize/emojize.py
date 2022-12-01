import emoji

text = input("emoji: ").strip()
if "_" in text:
    print(emoji.emojize(text))
else:
    print(emoji.emojize(text, language="alias"))
