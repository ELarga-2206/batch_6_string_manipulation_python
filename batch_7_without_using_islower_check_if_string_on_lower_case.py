#  islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

def is_all_lower(text):
    for char in text:
        if char.isalpha() and not (97 <= ord(char) <= 122):
            return False
    return bool(text)

user_input = input("Enter a string to check: ")

if is_all_lower(user_input):
    print("lowercase")
else:
    print("NOT all lowercase")