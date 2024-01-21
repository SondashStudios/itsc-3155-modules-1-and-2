#Developer: Caius Iliesi
#Date: 1/16/2024

# Initialize an empty list to store all numbers
all_numbers = []

# Take input from the user until "QUIT" is entered
while True:
    user_input = input("Enter a number or QUIT to quit: ")

    if user_input.upper() == "QUIT":
        break

    try:
        number = int(user_input)
        all_numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Create a list of even numbers
even_numbers = [num for num in all_numbers if num % 2 == 0]

# Print both lists
print("All Nums: ", all_numbers)
print("Even Nums: ", even_numbers)