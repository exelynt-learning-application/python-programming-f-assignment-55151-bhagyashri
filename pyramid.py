# number_pyramid_analysis.py

# Function to create a pyramid and calculate sums
def number_pyramid_analysis(n):
    total_numbers = 0
    total_sum = 0
    even_sum = 0

    # Printing the pyramid with all numbers (no filtering here)
    print("\nNumber Pyramid:")
    for i in range(1, n + 1):
        # Printing leading spaces for alignment
        print(" " * (n - i), end="")  # Spaces to align the pyramid
        
        # Printing the numbers in each row
        for j in range(1, i + 1):
            print(j, end=" ")  # Printing the number in the current row
            
            # Counting all numbers printed
            total_numbers += 1  # Count all numbers printed
            total_sum += j  # Add number to total sum
            
        # Move to the next line after each row
        print()

    # After pyramid printing, calculate sums separately
    print("\nAnalysis of the Pyramid:")

    # Calculate sum of even numbers while skipping odd numbers
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j > 10:  # Stop sum calculation if number exceeds 10
                break
            if j % 2 != 0:  # Skip odd numbers
                continue
            even_sum += j  # Add even number to even sum

    print(f"Total numbers printed: {total_numbers}")
    print(f"Sum of all numbers: {total_sum}")
    print(f"Sum of even numbers: {even_sum}")

# Main function to get user input and call the number_pyramid_analysis function
def main():
    while True:
        try:
            n = int(input("Enter a positive integer for the number of rows in the pyramid: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    # Calling the function to create pyramid and perform analysis
    number_pyramid_analysis(n)

if __name__ == "__main__":
    main()