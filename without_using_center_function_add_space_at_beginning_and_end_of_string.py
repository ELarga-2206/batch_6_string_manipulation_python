#center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

def custom_center(text, width, fill=' '):
    padding = width - len(text)
    return fill * (padding // 2) + text + fill * (padding - padding // 2)

text = input("Enter text: ")
width = int(input("Enter width: "))
print(f"Result: '{custom_center(text, width)}'")