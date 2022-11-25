# Take user input (without surrounding spaces and convert to lowercase)
file = input("File Name: ").strip().lower()

# print result using if-else blocks
# Use endswith
if file.endswith(".gif"):
    print("image/gif")

elif file.endswith(".jpeg") or file.endswith(".jpg"):
    print("image/jpeg")

elif file.endswith(".png"):
    print("image/png")

elif file.endswith(".pdf"):
    print("application/pdf")

elif file.endswith(".txt"):
    print("text/plain")

elif file.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")
