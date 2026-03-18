# Basic Calculator Program

# Constants for assignment operations
ADJUSTMENT_VALUE = 5  # Value to add to num1
MULTIPLIER = 2  # Value to multiply num1 by
SUBTRACTION_VALUE = 2  # Value to subtract from num2

# Taking two numbers from the user
num1 = float(input("Enter the first number: "))  # Taking the first number and converting to float
num2 = float(input("Enter the second number: "))  # Taking the second number and converting to float

# Perform arithmetic operations before assignment operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
# Handle division by zero
if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
else:
    division = "Undefined (division by zero)"
    modulus = "Undefined (modulus by zero)"

# Use assignment operators to perform arithmetic operations and update values
num1 += ADJUSTMENT_VALUE  # Adding the constant value to num1
num2 -= SUBTRACTION_VALUE  # Subtracting the constant value from num2
num1 *= MULTIPLIER  # Multiplying num1 by the constant multiplier

# Print original arithmetic results
print("\n--- Calculator Results (Before Assignment Operations) ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")

# Display the updated values of num1 and num2 after assignment operations
print(f"\nUpdated values after assignment operations: num1 = {num1}, num2 = {num2}")