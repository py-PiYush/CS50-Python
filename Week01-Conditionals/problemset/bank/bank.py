# Take user input
greet = input("Greeting: ")

# strip off surrounding white spaces and make it case-insensitive
greet = greet.strip().lower()

# $0 if greeting is hello
if greet.startswith("hello"):
    print("$0")

# $20 if greeting starts with 'h'
elif greet.startswith("h"):
    print("$20")

# $100 otherwise
else:
    print("$100")
