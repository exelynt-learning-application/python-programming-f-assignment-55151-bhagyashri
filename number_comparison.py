# Number Comparison Program

# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))  # Convert input to float for more flexibility
num2 = float(input("Enter the second number: "))  # Convert input to float

# Check which number is greater
is_num1_greater = num1 > num2
is_num2_greater = num2 > num1

# Check if both numbers are equal
are_numbers_equal = num1 == num2

# Check if both numbers are positive
are_both_positive = (num1 > 0) and (num2 > 0)

# Using logical operators (and, or, not) for comparisons
# Example: checking if both numbers are either positive or equal
positive_or_equal = (num1 > 0 or num2 > 0) and not are_numbers_equal

# Displaying the results
print("\n--- Comparison Results ---")
print(f"Is num1 greater than num2? {is_num1_greater}")
print(f"Is num2 greater than num1? {is_num2_greater}")
print(f"Are num1 and num2 equal? {are_numbers_equal}")
print(f"Are both numbers positive? {are_both_positive}")
print(f"Are either of the numbers positive or both numbers equal? {positive_or_equal}")