#isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

#FUNCTION is_all_uppercase(string):
#IF string is empty:
# RETURN False
# FOR each character IN string:
# IF character is alphabetic:
# IF character's ASCII value is NOT between 65 ('A') and 90 ('Z'):
# RETURN False
# RETURN True  # All alphabetic chars are uppercase

def is_all_uppercase(s):
    for char in s:
        if char.isalpha() and not (65 <= ord(char) <= 90):
            return False
        return bool(s) 