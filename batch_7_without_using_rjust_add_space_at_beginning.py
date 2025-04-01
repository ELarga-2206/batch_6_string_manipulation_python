#rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

#FUNCTION custom_rjust(text, width, fill_char=' '):
# padding = width - LENGTH(text)
# IF padding > 0:
# RETURN (fill_char * padding) + text
# ELSE:
# RETURN text
# END FUNCTION