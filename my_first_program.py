# My First Python Program

# Asking the user to enter their details

# Ask for the user's name (string)
name = input("Please enter your name: ")

# Ask for the user's age (integer)
age = input("Please enter your age: ")

# Ask for the user's height in meters (float)
height = input("Please enter your height in meters: ")

# Ask for the user's favorite number (can be an integer or float)
favorite_number = input("Please enter your favorite number: ")

# Type casting the user inputs to the correct data types
age = int(age)  # Converting age to an integer
height = float(height)  # Converting height to a float
favorite_number = float(favorite_number)  # Converting favorite number to a float (can also be an integer)

# Displaying the user's details in a formatted output
print("\n--- User Profile ---")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Height: {height} meters")
print(f"Favorite Number: {favorite_number}")

# Display the data type of each variable using type()
print("\n--- Data Types ---")
print(f"Data type of name: {type(name)}")
print(f"Data type of age: {type(age)}")
print(f"Data type of height: {type(height)}")
print(f"Data type of favorite_number: {type(favorite_number)}")

# Perform an arithmetic operation (add age and favorite number)
sum_of_age_and_favorite_number = age + favorite_number

# Display the result of the arithmetic operation with a meaningful message
print(f"\nThe sum of your age and favorite number is: {sum_of_age_and_favorite_number}")
