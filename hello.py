# Hello World Python Program

# Taking user input using the input() function
name = input("Please enter your name: ")  # Asking for the user's name
age = input("Please enter your age: ")  # Asking for the user's age
city = input("Please enter your city: ")  # Asking for the user's city

# Converting the input values where necessary
age = int(age)  # Converting age to an integer (since input returns a string)

# Displaying the user information using formatted output
print("\n--- User Profile ---")
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"You live in {city}.")

# Program successfully displays the user's information in a clear, readable format
