# menu_calculator.py

def menu():
    print("Menu: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting the program.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            match choice:
                case "1":
                    result = add(num1, num2)
                case "2":
                    result = subtract(num1, num2)
                case "3":
                    result = multiply(num1, num2)
                case "4":
                    result = divide(num1, num2)
                case _:
                    result = "Invalid choice, please try again."
                    print(result)
                    continue

            print(f"Result: {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()