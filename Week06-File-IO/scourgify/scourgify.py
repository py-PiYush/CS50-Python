import sys
import csv

# Take valid file from command-line
# Check for number of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Check for valid file type
file_name_read = sys.argv[1]
file_name_write = sys.argv[2]

if len(file_name_read) <= 4 or (
    len(file_name_read) > 4 and file_name_read[-4:] != ".csv"
):
    sys.exit("Not a CSV file")

write_list = []
# Open file
try:
    with open(file_name_read, "r") as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            last_first, house = row["name"], row["house"]
            last_first = last_first.replace('"', "")
            last, first = last_first.split(", ")
            write_list.append({"first": first, "last": last, "house": house})
# Check for non-existent file
except FileNotFoundError:
    sys.exit(f"Could not read {file_name_read}")

# Write to the new file in updated format
with open(file_name_write, "w") as write_file:
    writer = csv.DictWriter(write_file, ["first", "last", "house"])
    writer.writeheader()
    for row in write_list:
        writer.writerow(row)
