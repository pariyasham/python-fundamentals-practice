# Write a program that receives a text and a word from the user.
# Then check whether the given word appears in the text,
# and display the result.

text = input("Enter the Text: ").lower()
word = input("What word are you looking for?: ").lower()

count = text.count(word)
count += text.count(word[::-1])


# This condition is added because if the user searches for a single character, it would be counted twice (once normally and once in reverse), so we correct that here.
if(len(word) == 1):
    count = int(count / 2)

if(count > 0):
    print(f'Yes,"{word}" appears    {count}    times in your text!')
else:
    print(f'No!')