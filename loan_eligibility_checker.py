# Loan Eligibility Checker Program

# Taking age and salary as input from the user
try:
    age = int(input("Enter your age: "))  # Taking the age as input and converting it to an integer
    salary = float(input("Enter your salary: "))  # Taking the salary as input and converting it to a float

    # Check eligibility using nested conditions
    if age >= 21:  # First condition: Check if the age is greater than or equal to 21
        if salary >= 25000:  # Nested condition: Check if the salary is greater than or equal to 25,000
            eligibility = "Eligible for loan"
        else:
            eligibility = "Not eligible for loan due to insufficient salary"
    else:
        eligibility = "Not eligible for loan due to age"

    # Display eligibility result
    print(f"\nEligibility result: {eligibility}")

except ValueError:
    print("Invalid input! Please enter valid numeric values for age and salary.")