# Type Conversion Practice Program

# Ask the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the inputs into appropriate data types
num1_int = int(num1)  # Convert first input to integer
num2_float = float(num2)  # Convert second input to float

# Perform arithmetic operations
addition = num1_int + num2_float
subtraction = num1_int - num2_float
multiplication = num1_int * num2_float
division = num1_int / num2_float

# Display the results of each operation
print("\n--- Arithmetic Results ---")
print(f"Addition: {num1_int} + {num2_float} = {addition}")
print(f"Subtraction: {num1_int} - {num2_float} = {subtraction}")
print(f"Multiplication: {num1_int} * {num2_float} = {multiplication}")
print(f"Division: {num1_int} / {num2_float} = {division}")

# Convert one numeric value into a string and print it with a message
num1_str = str(num1_int)
print(f"\nConverted value into string: '{num1_str}' with a message")

# Show the data type of each converted value using type()
print("\n--- Data Types of Converted Values ---")
print(f"Data type of num1 (int): {type(num1_int)}")
print(f"Data type of num2 (float): {type(num2_float)}")
print(f"Data type of num1_str (string): {type(num1_str)}")
