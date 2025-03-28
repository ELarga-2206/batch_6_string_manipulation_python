#ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

def custom_ljust(s, width, fillchar=' '):
    if len(s) >= width:
        return s
    return s + (fillchar * (width - len(s)))

text = input("Enter text: ")
width = int(input("Enter width: "))
fill = input("Enter fill character (press Enter for space): ") or ' '

result = custom_ljust(text, width, fill[:1])  # Use only first char if multiple provided
print(f"\nResult: '{result}'")
print(f"Length: {len(result)} characters")