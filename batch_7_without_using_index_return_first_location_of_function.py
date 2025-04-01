# index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

#FUNCTION custom_index(text, substring):
# sub_length = LENGTH(substring)
# text_length = LENGTH(text)
# 
# IF sub_length == 0:
# RETURN 0
# 
# FOR i FROM 0 TO (text_length - sub_length):
# Check if current slice matches substring
# IF text[i TO i+sub_length] == substring:
# RETURN i ---First match found

