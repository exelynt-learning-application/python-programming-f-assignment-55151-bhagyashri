# Interactive User Profile Program

# Collecting user details using input() function
name = input("Please enter your name: ")  # Storing the name input
age = input("Please enter your age: ")  # Storing the age input
course = input("Please enter your course name: ")  # Storing the course input
email = input("Please enter your email address: ")  # Storing the email input

# Converting age to an integer since input() returns a string by default
age = int(age)

# Output the collected information in a formatted manner
print("\n--- User Profile ---")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Course: {course}")
print(f"Email: {email}")

# Program successfully prints the user's details in a clear, readable format
