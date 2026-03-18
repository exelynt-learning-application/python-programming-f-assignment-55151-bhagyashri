# Basic Calculator Program

# Taking two numbers from the user
num1 = float(input("Enter the first number: "))  # Taking the first number and converting to float
num2 = float(input("Enter the second number: "))  # Taking the second number and converting to float

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

# Using assignment operators to perform arithmetic operations and update values
num1 += 5  # Adding 5 to num1
num2 -= 2  # Subtracting 2 from num2
num1 *= 2  # Multiplying num1 by 2

# Printing all results clearly
print("\n--- Calculator Results ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")

# Displaying the updated values of num1 and num2 after assignment operations
print(f"\nUpdated values: num1 = {num1}, num2 = {num2}")