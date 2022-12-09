import sys
from PIL import Image, ImageOps

# Take valid file from command-line
# Check for number of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Check for valid file type
file_name_read = sys.argv[1]
file_name_write = sys.argv[2]

if not (
    file_name_read.lower().endswith(".jpg")
    or file_name_read.lower().endswith(".jpeg")
    or file_name_read.lower().endswith(".png")
):
    sys.exit("Invalid Input")

if not (
    file_name_write.lower().endswith(".jpg")
    or file_name_write.lower().endswith(".jpeg")
    or file_name_write.lower().endswith(".png")
):
    sys.exit("Invalid Output")

# same file type
if file_name_read[-3:] != file_name_write[-3:]:
    sys.exit("Input and output have different extensions")


shirt = Image.open("shirt.png")
shirt_size = shirt.size
# Open file
try:
    with Image.open(file_name_read, "r") as read_file:
        # Resize the image to that of shirt.png
        read_file = ImageOps.fit(read_file, shirt_size)
        # Paste shirt.png on this image
        read_file.paste(shirt, shirt)
        # Save the new image
        read_file.save(file_name_write)

except FileNotFoundError:
    sys.exit("Input does not exist")
