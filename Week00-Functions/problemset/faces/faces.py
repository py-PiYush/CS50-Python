# Main function
def main():

    # Get user input
    text = input("Enter text: ")

    # Convert
    converted_text = convert(text)

    # Print result
    print(converted_text)


# Function to convert emoticons to emojis


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()
