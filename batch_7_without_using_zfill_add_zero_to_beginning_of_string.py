# zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

def custom_zfill(text, width):
    zeros_needed = width - len(text)
    if zeros_needed > 0:
        return '0' * zeros_needed + text
    return text

text = input("Enter a string: ")
width = int(input("Enter total width: "))

result = custom_zfill(text, width)

print(f"Result: '{result}'")