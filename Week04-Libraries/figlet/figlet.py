import sys
import random
from pyfiglet import Figlet

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid Usage")
if len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid Usage")

# Get font
figlet = Figlet()
font_list = figlet.getFonts()
if len(sys.argv) == 1:
    f = random.choice(font_list)
else:
    f = sys.argv[2]
    if f not in font_list:
        sys.exit("Invalid Usage")

# Get user input
text = input("Input: ").strip()

# Set font and print
figlet.setFont(font=f)
print(figlet.renderText(text))
