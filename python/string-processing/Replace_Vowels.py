# This program takes a text input from the user and processes each word individually.
# It replaces every 'A'/'a' with '*' and every 'E'/'e' with '#'.
# After modifying the letters, it ensures that the first character of each word is uppercase.
# Finally, it prints the transformed words back together as a single sentence.

text = input("Enter Your Text: ").split()
finally_text = []
for word in text:
    modified_word = []
    for char in word:
        if char == 'A' or char == 'a':
            modified_word.append('*')
        elif char == 'E' or char == 'e':
            modified_word.append('#')
        else:
            modified_word.append(char)
    
    if modified_word:
        modified_word[0] = modified_word[0].upper()
    
    finally_text.append(''.join(modified_word))
print(' '.join(finally_text))