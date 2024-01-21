#Caius Iliesi
#Date: 1/21/2024

user_input = input("Enter a string: ")

# Separate uppercase and lowercase letters
uppercase_letters = ''.join([char for char in user_input if char.isupper()])
lowercase_letters = ''.join([char for char in user_input if char.islower()])
other_characters = ''.join([char for char in user_input if not char.isalpha()])

# Concatenate lowercase letters, uppercase letters, and other characters
result_string = lowercase_letters + uppercase_letters + other_characters

print("Modified String:", result_string)