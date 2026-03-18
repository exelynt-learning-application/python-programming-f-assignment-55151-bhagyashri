# Student Grade Calculator Program

# Taking marks as input from the user
try:
    marks = float(input("Enter the marks obtained by the student: "))  # Convert input to float for flexibility

    # Check if marks are valid (between 0 and 100)
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a number between 0 and 100.")
    else:
        # Assign grades based on the marks
        if marks >= 90:
            grade = 'A'
            result = "Pass"
        elif marks >= 75:
            grade = 'B'
            result = "Pass"
        elif marks >= 60:
            grade = 'C'
            result = "Pass"
        else:
            grade = 'Fail'
            result = "Fail"

        # Display grade and result
        print(f"\nStudent Grade: {grade}")
        print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter a valid number for marks.")