# rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

#FUNCTION custom_rindex(text, substring):
# sub_length = LENGTH(substring)
# text_length = LENGTH(text)
#  Start from the end and move left
# FOR i FROM (text_length - sub_length) DOWN TO 0:
# IF text[i TO i+sub_length] == substring:
# RETURN i --- Last match found

def custom_rindex(text, substring):
    sub_len = len(substring)
    for i in range(len(text) - sub_len, -1, -1):
        if text[i:i+sub_len] == substring:
            return i