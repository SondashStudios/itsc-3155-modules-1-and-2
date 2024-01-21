#Developer: Caius Iliesi
#Date: 1/16/2024

# Initialize an empty list to store user input
original_list = []

# Take input from the user for 10 integers
for _ in range(10):
    while True:
        try:
            number = int(input("Enter number: "))
            original_list.append(number)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Create a new list with only elements that appear once
unique_elements = [num for num in original_list if original_list.count(num) == 1]

# Print both lists
print("Original List: ", original_list)
print("Nums that appear once: ", unique_elements)