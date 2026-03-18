# number_pyramid_analysis.py

# Function to create a pyramid and calculate sums
def number_pyramid_analysis(n):
    total_numbers = 0
    total_sum = 0
    even_sum = 0

    # Flag variable to stop all processing when a number greater than 10 is encountered
    stop_processing = False

    # Printing the pyramid
    print("\nNumber Pyramid:")
    for i in range(1, n + 1):
        # If processing is stopped, break the outer loop as well
        if stop_processing:
            break

        # Printing leading spaces for alignment
        print(" " * (n - i), end="")  # Spaces to align the pyramid
        
        # Printing the numbers in each row
        for j in range(1, i + 1):
            # Check for number greater than 10 and stop all processing
            if j > 10:
                stop_processing = True
                break  # Break the inner loop when j > 10
            
            # Skip odd numbers and add to the sum only for even numbers
            if j % 2 != 0:
                continue  # Skip odd numbers
            
            # Counting even numbers and adding to sums
            total_numbers += 1  # Count every even number printed
            total_sum += j  # Add even number to total sum
            even_sum += j  # Add even number to even sum

            print(j, end=" ")  # Printing the even number in the current row
        
        # Move to the next line after each row
        print()

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