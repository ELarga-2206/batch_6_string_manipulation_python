#  islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

#F0UNCTION is_all_lower(text):
# IF text is empty: RETURN False
# 
# FOR each character IN text:
# IF character is a letter AND NOT lowercase:
# RETURN False

def is_all_lower(text):
    for char in text:
        if char.isalpha() and not (97 <= ord(char) <= 122):
            return False
    return bool(text)