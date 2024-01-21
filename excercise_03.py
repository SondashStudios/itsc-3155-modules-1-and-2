#Developer: Caius Iliesi
#Date: 1/16/2024

# Take input from the user
n = int(input("Enter an integer greater than 1: "))

# Print the cubes of integers from 0 to n
for i in range(n + 1):
    print(f"The cube of {i} is {i**3}")