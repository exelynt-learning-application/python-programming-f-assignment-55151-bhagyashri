# Number Comparison Program

# Function to compare two numbers and display results
def compare_numbers(num1, num2):
    # Check which number is greater
    is_num1_greater = num1 > num2
    is_num2_greater = num2 > num1

    # Check if both numbers are equal
    are_numbers_equal = num1 == num2

    # Check if both numbers are positive
    are_both_positive = num1 > 0 and num2 > 0

    # Using logical operators (and, or, not) for comparisons
    positive_or_equal = (num1 > 0 or num2 > 0) or are_numbers_equal

    # Displaying the results
    print("\n--- Comparison Results ---")
    print(f"Is num1 greater than num2? {is_num1_greater}")
    print(f"Is num2 greater than num1? {is_num2_greater}")
    print(f"Are num1 and num2 equal? {are_numbers_equal}")
    print(f"Are both numbers positive? {are_both_positive}")
    print(f"Are either of the numbers positive or both numbers equal? {positive_or_equal}")


# Taking input from the user for two numbers
try:
    num1 = float(input("Enter the first number: "))  # Convert input to float for flexibility
    num2 = float(input("Enter the second number: "))  # Convert input to float for flexibility

    # Input validation to check if the entered values are valid numbers
    if num1 != num1 or num2 != num2:  # Check for NaN (Not-a-Number)
        print("Please enter valid numeric values.")
    else:
        # Call the function to compare the numbers
        compare_numbers(num1, num2)
except ValueError:
    print("Please enter valid numeric values.")