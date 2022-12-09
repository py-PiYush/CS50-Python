import sys

# Take valid file from command-line
# Check for number of command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check for valid file type
file_name = sys.argv[1]
if len(file_name) <= 3 or (len(file_name) > 3 and file_name[-3:] != ".py"):
    sys.exit("Not a python file")

# Open file
try:
    file = open(file_name)
# Check for non-existent file
except FileNotFoundError:
    sys.exit("File does not exist")

line_count = 0

# Read file
for line in file:
    # Remove whitespaces
    line = line.strip()
    # Check for non-comments and non-empty characters
    if len(line) > 0 and line[0] != "#":
        line_count += 1

print(line_count)
