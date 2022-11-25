c = 300000000

# Ask user for mass
mass = int(input("Enter mass of the object: "))

# Convert to Energy using E = mc^2
energy = mass * pow(c, 2)

print(energy)
