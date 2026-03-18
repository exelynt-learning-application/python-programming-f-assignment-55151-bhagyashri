# conditional_logic_practice_set.py

# Problem 1: Check whether a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Problem 2: Check whether a year is a leap year
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."

# Problem 3: Find the largest of three numbers
def largest_of_three(num1, num2, num3):
    largest = max(num1, num2, num3)
    return f"The largest number is {largest}."

# Problem 4: Check whether a number is positive, negative, or zero
def check_sign(number):
    if number > 0:
        return f"{number} is positive."
    elif number < 0:
        return f"{number} is negative."
    else:
        return f"{number} is zero."

# Problem 5: Determine pass/fail based on marks
def check_pass_fail(marks):
    if marks >= 50:
        return f"Congratulations! You passed with {marks}%."
    else:
        return f"Sorry, you failed with {marks}%. Better luck next time."

def main():
    # Test cases for each problem
    print("Problem 1: Check Even or Odd")
    number = int(input("Enter a number: "))
    print(check_even_odd(number))
    
    print("\nProblem 2: Check Leap Year")
    year = int(input("Enter a year: "))
    print(check_leap_year(year))
    
    print("\nProblem 3: Largest of Three Numbers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    print(largest_of_three(num1, num2, num3))
    
    print("\nProblem 4: Check Positive, Negative, or Zero")
    number = float(input("Enter a number: "))
    print(check_sign(number))
    
    print("\nProblem 5: Determine Pass/Fail")
    marks = float(input("Enter your marks: "))
    print(check_pass_fail(marks))

if __name__ == "__main__":
    main()