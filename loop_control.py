# loop_control.py

# Using a for loop to iterate over numbers 1 to 10
for number in range(1, 11):
    # Skip even numbers using continue
    if number % 2 == 0:
        continue
    
    # Stop the loop at number 8 using break
    if number == 8:
        print(f"Stopping at {number}")
        break
    
    # Using pass statement inside an if block
    if number == 5:
        pass  # Do nothing for number 5
    
    # Print the current number
    print(number)