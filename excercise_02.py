#Developer: Caius Iliesi
#Date: 1/16/2024

string1 = input("Enter a string: ")
string2 = input("Enter another string: ")

# Check if one string is the suffix of the other
if string1.endswith(string2) or string2.endswith(string1):
    print("True")
else:
    print("False")