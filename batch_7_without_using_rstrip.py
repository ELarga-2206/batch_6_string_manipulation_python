# rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# FUNCTION custom_rstrip(text):
# end = LENGTH(text)
# WHILE end > 0 AND text[end-1] == ' ':
# end = end - 1
# RETURN text[FROM START TO end]
# END FUNCTION

# DISPLAY "Enter a string with trailing spaces:"
# GET user_input
# result = CALL custom_rstrip(user_input)
# DISPLAY "Original:", user_input
# DISPLAY "Stripped:", result
# END PROGRAM

def custom_rstrip(text):
    end = len(text)
    while end > 0 and text[end-1] == ' ':
        end -= 1
    return text[:end]