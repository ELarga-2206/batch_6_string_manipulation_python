# upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# FUNCTION custom_upper(text):
# result = EMPTY_STRING
# FOR EACH character IN text:
# IF character is lowercase letter (a-z):
#  Convert to uppercase using ASCII
# uppercase_char = CHARACTER(ASCII(character) - 32)
# ADD uppercase_char TO result
# ELSE:
# ADD character TO result  // Keep non-lowercase chars unchanged
# RETURN result

def custom_upper(text):
    result = []
    for char in text:
        if 97 <= ord(char) <= 122:
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)
    return ''.join(result)