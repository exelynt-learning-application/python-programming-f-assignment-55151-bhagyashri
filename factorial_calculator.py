# factorial_calculator.py

# Taking a positive integer input from the user
number = int(input("Enter a positive integer: "))

# Check if the number is positive
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Initializing the factorial result to 1 (since factorial of 0 and 1 is 1)
    factorial = 1

    # Using a for loop to calculate the factorial
    for i in range(1, number + 1):
        factorial *= i  # Multiply the current number to the result

    # Displaying the factorial result
    print(f"The factorial of {number} is {factorial}.")