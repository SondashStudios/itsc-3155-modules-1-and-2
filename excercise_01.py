#Developer: Caius Iliesi
#Date: 1/16/2024

# Take input from the user
grade = int(input("Enter a grade from 0  to 100: "))

# Determine the letter grade
if 90 <= grade <= 100:
    print("Your grade is A")
elif 80 <= grade < 90:
    print("Your grade is B")
elif 70 <= grade < 80:
    print("Your grade is C")
elif 60 <= grade < 70:
    print("Your grade is D")
else:
    print("Your grade is F")