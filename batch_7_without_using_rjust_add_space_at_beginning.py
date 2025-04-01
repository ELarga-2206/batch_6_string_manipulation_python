#rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

def custom_rjust(text, width, fill_char=' '):
    padding = width - len(text)
    return fill_char * padding + text if padding > 0 else text

text = input("Enter text: ")
width = int(input("Enter width: "))
fill = input("Enter fill character (space by default): ") or ' '

result = custom_rjust(text, width, fill[:1])  # Use only first char if multiple provided

print(f"Result: '{result}' (Length: {len(result)})")