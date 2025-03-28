#lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

def to_lowercase(s):
    result = []
    for char in s:
        if 65 <= ord(char) <= 90:
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)
    return ''.join(result)
    
user_input = input("Enter a string to convert to lowercase: ")

lowercase_output = to_lowercase(user_input)
print("\nLowercase result:")
print(lowercase_output)