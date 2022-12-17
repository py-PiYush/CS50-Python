from validator_collection import validators, checkers

email = input("Email: ").strip()
is_email = checkers.is_email(email)
if is_email:
    print("Valid")
else:
    print("Invalid")
