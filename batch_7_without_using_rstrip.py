# rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

def custom_rstrip(text):
    end = len(text)
    while end > 0 and text[end-1] == ' ':
        end -= 1
    return text[:end]

user_input = input("Enter a string with trailing spaces: ")

result = custom_rstrip(user_input)

print(f"Original: '{user_input}'")
print(f"Stripped: '{result}'")