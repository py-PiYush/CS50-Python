import sys
from tabulate import tabulate

# Take valid file from command-line
# Check for number of command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check for valid file type
file_name = sys.argv[1]
if len(file_name) <= 4 or (len(file_name) > 4 and file_name[-4:] != ".csv"):
    sys.exit("Not a CSV file")

table_list = []
# Open file
try:
    with open(file_name, "r") as file:
        for row in file:
            table_list.append(row.strip().split(","))
# Check for non-existent file
except FileNotFoundError:
    sys.exit("File does not exist")

# Print ASCII art using tabulate
print(tabulate(table_list, headers="firstrow", tablefmt="grid"))
