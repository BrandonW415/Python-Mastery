sentence = input("Enter a sentence: ")
print(sentence.upper())

paragraph = input("Enter a paragraph: ")
words = paragraph.split()
print(f"Number of words: {len(words)}")

string = input("Enter a string to check if all characters are digits: ")
print(string.isdigit())

string = input("Enter a string to replace 'a' with 'o': ")
print(string.replace('a', 'o'))

full_name = input("Enter your full name: ")
initials = '.' .join(name[0].upper() for name in full_name.split())
print(f"Your initials are: {initials}")

string = input("Enter a string to get its length: ")
print(f"The length of your string is: {len(string)}")