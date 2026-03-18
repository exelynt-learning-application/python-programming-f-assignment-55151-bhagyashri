# nested_loops_table.py

# Outer loop iterates over the range 1 to 5 for rows
for i in range(1, 6):
    # Inner loop iterates over the range 1 to 5 for columns
    for j in range(1, 6):
        # Printing the product of i and j, with a tab space for readability
        print(f"{i * j}\t", end="")  # end="" prevents moving to a new line after each print
        
    # After the inner loop ends, print a new line to start the next row
    print()