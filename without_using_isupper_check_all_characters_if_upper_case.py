#isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

def is_all_uppercase(s):
    for char in s:
        if char.isalpha() and not (65 <= ord(char) <= 90):
            return False
        return bool(s) 
    
user_input = input("Enter a string to check: ")

if is_all_uppercase(user_input):
    print("uppercase")
else:
    print("not uppercase")