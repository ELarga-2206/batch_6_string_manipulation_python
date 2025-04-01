# index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

def custom_index(text, substring):
    sub_len = len(substring)
    for i in range(len(text) - sub_len + 1):
        if text[i:i+sub_len] == substring:
            return i 
        
text = input("Enter the main text: ")
sub = input("Enter the substring to find: ")

position = custom_index(text, sub)
if position != -1:
    print(f"Found at position: {position}")
else:
    print("Substring not found")