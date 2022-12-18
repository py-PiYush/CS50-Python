from fpdf import FPDF

# Get user name
name = input("Name: ").strip()

pdf = FPDF()

# Add page
pdf.add_page()

# Set font of header
pdf.set_font("Times", "B", 16)

# Add header
pdf.cell(190, 0, "CS50 SHIRTIFICATE", new_x="LMARGIN", new_y="NEXT", align="C")

# add shirt
pdf.image("shirtificate.png", x=10, y=50, w=190)

# print in shirt
pdf.set_text_color(r=255, g=215, b=255)
pdf.cell(190, 200, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
