#Developer: Caius Iliesi
#Date: 1/16/2024

# Take input from the user
n = int(input("Enter a number: "))

# Initialize an empty list to store floats
float_list = []

# Take n floats from the user and store them in the list
for i in range(1, n + 1):
    float_number = float(input(f"Enter number {i}: "))
    float_list.append(float_number)

# Print the list
print("List: ", float_list)

# Calculate and print the mean/average
mean = sum(float_list) / len(float_list)
print("Average:", mean)