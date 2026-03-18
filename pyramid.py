# number_pyramid_analysis.py

# Function to create a pyramid and calculate sums
def number_pyramid_analysis(n):
    total_numbers = 0
    total_sum = 0
    even_sum = 0

    # Flag to stop all processing when a number > 10 is encountered
    stop_processing = False

    # Printing the pyramid with all numbers (no filtering here)
    print("\nNumber Pyramid:")
    for i in range(1, n + 1):
        # If processing should stop, break the outer loop as well
        if stop_processing:
            break

        # Printing leading spaces for alignment
        print(" " * (n - i), end="")  # Spaces to align the pyramid
        
        # Printing the numbers in each row
        row_numbers = []  # Store the numbers in the row to print later
        for j in range(1, i + 1):
            if j > 10:  # Stop printing if number exceeds 10
                stop_processing = True
                break
            row_numbers.append(str(j))  # Store number as string for proper formatting

        print(" ".join(row_numbers))  # Print the row with no trailing space

        # Update the total numbers and total sum after printing the pyramid
        total_numbers += len(row_numbers)  # Count the numbers in the row
        total_sum += sum(range(1, i + 1))  # Sum all numbers in the row

    # After pyramid printing, calculate sums for even numbers separately
    even_sum = sum(j for j in range(1, 11) if j % 2 == 0)

    # Displaying analysis after pyramid and sum calculation
    print("\nAnalysis of the Pyramid:")
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