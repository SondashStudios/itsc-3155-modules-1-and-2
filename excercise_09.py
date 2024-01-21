#Developer: Caius Iliesi
#Date: 1/16/2024

# Initialize an empty list to store words
word_list = []

# Take input from the user for 5 words
for _ in range(5):
    word = input("Enter a word: ")
    word_list.append(word)

# Create a single string from the list, separated by spaces
resultant_string = " ".join(word_list)

# Print both the list and the resultant string
print("Words: ", word_list)
print("One String: ", resultant_string)