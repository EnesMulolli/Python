# Create a list
names = ["Blerta", "Erosi", "Driloni", "Brikena", "Ylli"]

# Loop through the list and print each name
for name in names:
    print(name)

# Sentence and print only alphabetic characters
sentence = "Hello World"
for character in sentence:
    if character.isalpha():  # Checks if the character is a letter
        print(character)

# Range function (example from 0 to 4)
for number in range(5):  # This will iterate from 0 to 4
    print(number)

# Finding the maximum value in the list of numbers
numbers = [12, 45, 6, 72, 8, 94, 57]
maximum = numbers[0]

for num in numbers:  # Loop through each element in the list "numbers"
    if num > maximum:  # Check if the current element "num" is greater than the current maximum value
        maximum = num  # If so, update the maximum value to be the current element in num

print("The maximum value in the list is", maximum)














