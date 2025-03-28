#lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

def custom_lstrip(text):
    start = 0
    while start < len(text) and text[start] == ' ':
        start += 1
    return text[start:]

user_input = input("Enter a string with leading spaces: ")

result = custom_lstrip(user_input)

print(f"Original: '{user_input}'")
print(f"Stripped: '{result}'")