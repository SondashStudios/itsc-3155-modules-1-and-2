#Developer: Caius Iliesi
#Date: 1/16/2024

# Take input from the user
input_string = input("Enter a string: ")

# Split the string into a list of single characters
char_list = list(input_string)

# Split the list of characters into a list of lists with 3 elements each
nested_list = [char_list[i:i+3] for i in range(0, len(char_list), 3)]

# Print only the resultant list of lists
print(nested_list)