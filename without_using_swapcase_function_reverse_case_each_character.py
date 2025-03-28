#swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

def swapcase(s):
    result = []
    for char in s:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

user_input = input("Enter a string to swap cases: ")

swapped_output = swapcase(user_input)
print("\nresult:")
print(swapped_output)