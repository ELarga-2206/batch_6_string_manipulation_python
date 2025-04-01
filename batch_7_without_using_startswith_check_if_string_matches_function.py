# startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

def custom_startswith(text, prefix):
    return text[:len(prefix)] == prefix

text = input("Enter the main text: ")
prefix = input("Enter the prefix to check: ")

if custom_startswith(text, prefix):
    print(f" The text starts with '{prefix}'")
else:
    print(f"The text does NOT start with '{prefix}'")