#Developer: Caius Iliesi
#Date: 1/16/2024

# Take input from the user for the first list
list1 = [int(input("Enter a number for the first list: ")) for _ in range(5)]

# Take input from the user for the first list
list2 = [int(input("Enter a number for the second list: ")) for _ in range(5)]

# Create a third array containing common values without duplicates
common_values = list(set(list1) & set(list2))

# Print all three lists
print("First List: ", list1)
print("Second List: ", list2)
print("Common List: ", common_values)