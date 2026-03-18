# range_even_numbers.py

# Using range() to generate even numbers between 2 and 50
# range(start, stop, step) generates numbers starting from 'start', up to but not including 'stop', with the given 'step'
# For even numbers, we start at 2, stop at 51 (since 50 should be included), and step by 2
for number in range(2, 51, 2):
    # Printing each even number in a new line
    print(number, end=" ")  # Using end=" " to print the numbers in a single line with spaces