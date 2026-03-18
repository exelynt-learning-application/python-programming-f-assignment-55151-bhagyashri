# star_pyramid.py

# The height of the pyramid is set to 5
height = 5

# Outer loop for the rows (1 to 5)
for i in range(1, height + 1):
    # Inner loop to print spaces for alignment
    for j in range(height - i):
        print(" ", end="")  # Printing spaces to align the stars
    
    # Inner loop to print stars
    for k in range(2 * i - 1):
        print("*", end="")  # Printing stars for the current row
    
    # Move to the next line after each row is printed
    print()