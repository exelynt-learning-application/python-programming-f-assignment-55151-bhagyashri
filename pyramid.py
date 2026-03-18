# number_pyramid_analysis.py

# Function to create a pyramid and calculate sums
def number_pyramid_analysis(n):
    total_numbers = 0
    total_sum = 0
    even_sum = 0

    # Flag to stop all processing when a number > 10 is encountered
    stop_processing = False

    # Printing the pyramid and calculating sums
    print("\nNumber Pyramid:")
    for i in range(1, n + 1):
        # Use break to stop the outer loop when flagged
        if stop_processing:
            break

        # Printing leading spaces for alignment
        print(" " * (n - i), end="")

        # Building the row numbers
        row_numbers = []
        for j in range(1, i + 1):
            if j > 10:  # Use break to stop when number exceeds 10
                stop_processing = True
                break
            row_numbers.append(j)

        print(" ".join(str(num) for num in row_numbers))

        # Calculate sums from actual printed numbers
        total_numbers += len(row_numbers)
        total_sum += sum(row_numbers)

        # Sum even numbers using continue to skip odd numbers
        for num in row_numbers:
            if num % 2 != 0:
                continue  # Skip odd numbers
            even_sum += num

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