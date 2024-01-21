#Developer: Caius Iliesi
#Date: 1/16/2024

# Take input from the user for row and column
row_number = int(input("Enter a row num from 1 to 5: "))
column_number = int(input("Enter a col num from 1 to 5: "))

# Validate input
if 1 <= row_number <= 5 and 1 <= column_number <= 5:
    # Create and print the grid
    for i in range(1, 6):
        for j in range(1, 6):
            if i == row_number and j == column_number:
                print(1, end=" ")
            else:
                print(0, end=" ")
        print()  # Move to the next row
else:
    print("Invalid input. Row and column numbers must be between 1 and 5 inclusive.")