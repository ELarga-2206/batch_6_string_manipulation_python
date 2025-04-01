# rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

def custom_rindex(text, substring):
    sub_len = len(substring)
    for i in range(len(text) - sub_len, -1, -1):
        if text[i:i+sub_len] == substring:
            return i
    raise ValueError("substring not found")  

text = input("Enter the main text: ")
sub = input("Enter the substring to find: ")

try:
    position = custom_rindex(text, sub)
    print(f"Last occurrence found at position: {position}")
except ValueError as e:
    print(e)