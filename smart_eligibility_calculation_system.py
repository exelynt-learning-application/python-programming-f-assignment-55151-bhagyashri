# smart_eligibility_calculation_system.py

# Function to check voting eligibility
def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Function to calculate student grade based on marks
def student_grade_calculator(marks):
    if marks >= 90:
        return "Grade: A"
    elif marks >= 75:
        return "Grade: B"
    elif marks >= 60:
        return "Grade: C"
    elif marks >= 50:
        return "Grade: D"
    else:
        return "Grade: F"

# Function for simple arithmetic calculations
def simple_calculator(num1, num2, operation):
    match operation:
        case "1":  # Addition
            return f"Result: {num1 + num2}"
        case "2":  # Subtraction
            return f"Result: {num1 - num2}"
        case "3":  # Multiplication
            return f"Result: {num1 * num2}"
        case "4":  # Division
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return f"Result: {num1 / num2}"
        case _:
            return "Invalid operation selected."

# Main menu function
def main():
    while True:
        # Displaying the menu
        print("\nSmart Eligibility & Calculation System")
        print("1. Check Voting Eligibility")
        print("2. Student Grade Calculator")
        print("3. Simple Calculator")
        print("4. Exit")
        
        # Taking user input for choice
        choice = input("Please select an option (1-4): ")

        if choice == "1":
            # Check Voting Eligibility
            try:
                age = int(input("Enter your age: "))
                if age < 0:
                    print("Error: Age cannot be negative.")
                else:
                    print(check_voting_eligibility(age))
            except ValueError:
                print("Error: Please enter a valid number for age.")
        
        elif choice == "2":
            # Student Grade Calculator
            try:
                marks = float(input("Enter the student's marks (0-100): "))
                if marks < 0 or marks > 100:
                    print("Error: Marks should be between 0 and 100.")
                else:
                    print(student_grade_calculator(marks))
            except ValueError:
                print("Error: Please enter a valid number for marks.")
        
        elif choice == "3":
            # Simple Calculator
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print("Select operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                operation = input("Enter your choice (1-4): ")
                print(simple_calculator(num1, num2, operation))
            except ValueError:
                print("Error: Please enter valid numbers for calculation.")
        
        elif choice == "4":
            # Exit program
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from 1 to 4.")

if __name__ == "__main__":
    main()