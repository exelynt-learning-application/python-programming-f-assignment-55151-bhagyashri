# string_datatype.py

# Defining strings
greeting = "Hello"
name = "Alice"

# Concatenating strings
message = greeting + " " + name
print(message)  # Output: "Hello Alice"

# String slicing
print(name[1:4])  # Output: "lic"

# String methods
print(message.upper())  # Output: "HELLO ALICE"
print(message.lower())  # Output: "hello alice"
print(message.replace("Alice", "Bob"))  # Output: "Hello Bob"

# Checking for substring
if "Alice" in message:
    print("Alice is in the message.")

# String length
print("Length of the message:", len(message))  # Output: Length of the message: 12