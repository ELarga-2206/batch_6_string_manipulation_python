# zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# FUNCTION custom_zfill(text, width):
# zeros_needed = width - LENGTH(text)
# IF zeros_needed > 0:
# RETURN ('0' * zeros_needed) + text
# ELSE:
# RETURN text
# END FUNCTION
# PROGRAM:
# DISPLAY "Enter a string:"
# GET text
# DISPLAY "Enter total width:"
# GET width
# result = CALL custom_zfill(text, width)
# DISPLAY "Result:", result