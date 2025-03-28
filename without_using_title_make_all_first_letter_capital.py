#title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

def simple_title(s):
    return ' '.join(word.capitalize() for word in s.split())

user_input = input("Enter a sentence to convert to title case: ")

title_case_output = simple_title(user_input)
print("\nConverted to title case:")
print(title_case_output)