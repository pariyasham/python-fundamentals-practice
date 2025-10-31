# Write a program that takes a word from the user,
# then receives a single character on the next line.
# The program should display the index (position) of that character
# within the given word.

word = input("Enter your word: ")
char = input("Enter your char: ")
try:
    index = word.index(char)
    print(index)
except ValueError:
    print("-1")