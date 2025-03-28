#lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

#FUNCTION custom_lstrip(text):
# start = 0
# WHILE start < length of text AND text[start] is space:
# start = start + 1
# RETURN text[start to end]
# END FUNCTION

# PROGRAM:
# DISPLAY "Enter a string with leading spaces:"
# user_input = GET input
# result = CALL custom_lstrip(user_input)
# DISPLAY "Original:", user_input
# DISPLAY "Stripped:", result