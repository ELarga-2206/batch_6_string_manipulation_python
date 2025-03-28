# capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

#FUNCTION custom_capitalize(text):
# IF text is empty:
# RETURN text  # Handle empty string case
# first_char = CONVERT text[0] TO UPPERCASE
# remaining_chars = CONVERT text[1:] TO LOWERCASE
# RETURN first_char + remaining_chars
# END FUNCTION

def custom_capitalize(text):
    if not text:  
        return text
    return text[0].upper() + text[1:].lower()

user_input = input("Enter a string: ")

result = custom_capitalize(user_input)

print("Capitalized result:", result)