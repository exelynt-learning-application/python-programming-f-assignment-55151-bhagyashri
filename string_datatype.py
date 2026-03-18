# string_datatype.py

# Defining strings with type annotations (in Python, type hints can be added for clarity)
greeting = "Hello"  # Type: str
name = "Alice"      # Type: str

# Concatenating strings
message = greeting + " " + name
print(message)  # Output: "Hello Alice"

# String slicing: Extracting a part of the string
print(name[1:4])  # Output: "lic"

# String methods:
print(message.upper())  # Output: "HELLO ALICE"
print(message.lower())  # Output: "hello alice"
print(message.replace("Alice", "Bob"))  # Output: "Hello Bob"

# Checking if a substring exists within a string
if "Alice" in message:
    print("Alice is in the message.")

# String length: Calculating the length of the string
print("Length of the message:", len(message))  # Output: Length of the message: 11