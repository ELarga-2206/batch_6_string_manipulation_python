# upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

def custom_upper(text):
    result = []
    for char in text:
        if 97 <= ord(char) <= 122:
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)
    return ''.join(result)

user_input = input("Enter a string: ")

uppercase_text = custom_upper(user_input)

print("Uppercase:", uppercase_text)