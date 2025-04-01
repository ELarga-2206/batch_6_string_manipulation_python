# count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# PROGRAM:
# DISPLAY "Enter the main text:"
# GET text FROM USER
# DISPLAY "Enter the substring to count:"
# GET substring FROM USER
# SET result = CALL custom_count(text, substring)
# DISPLAY "The substring appears " + result + " times"

#FUNCTION custom_count(text, substring):
# SET count = 0
# SET sub_len = LENGTH(substring)

# FOR i FROM 0 TO LENGTH(text) - sub_len:
# IF text[i TO i+sub_len] EQUALS substring:
# INCREMENT count BY 1
# 
#RETURN count