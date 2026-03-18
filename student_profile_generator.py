# Student Profile Generator Program

# Storing student details in variables
student_name = "John Doe"  # string
age = 20  # integer
course_fee = 1500.50  # float
is_enrolled = True  # boolean

# Printing student details in a readable format
print("Student Profile:")
print(f"Name: {student_name}")
print(f"Age: {age}")
print(f"Course Fee: ${course_fee}")
print(f"Enrolled: {is_enrolled}")

# Displaying the data type of each variable using the type() function
print("\nData Types:")
print(f"Type of student_name: {type(student_name)}")
print(f"Type of age: {type(age)}")
print(f"Type of course_fee: {type(course_fee)}")
print(f"Type of is_enrolled: {type(is_enrolled)}")

# Update: Incrementing the student's age by 1
age += 1  # dynamic update of age

# Update: Changing enrollment status
is_enrolled = False  # dynamic update of enrollment status

# Perform simple operation: Add a 10% tax to the course fee
tax_rate = 0.10
course_fee += course_fee * tax_rate  # adding tax

# Printing updated values and their data types again
print("\nUpdated Student Profile:")
print(f"Updated Age: {age}")
print(f"Updated Enrollment Status: {is_enrolled}")
print(f"Updated Course Fee: ${course_fee}")

# Display the updated data types
print("\nUpdated Data Types:")
print(f"Type of age: {type(age)}")
print(f"Type of is_enrolled: {type(is_enrolled)}")
print(f"Type of course_fee: {type(course_fee)}")
