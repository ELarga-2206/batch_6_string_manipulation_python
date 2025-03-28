#ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

#DISPLAY "Enter text to justify:"
# GET text from user
# DISPLAY "Enter total width:"
# GET width from user
# DISPLAY "Enter fill character (press Enter for space):"
# GET fill_input from user
# IF fill_input is empty:
# SET fillchar = ' '
# ELSE:
# SET fillchar = first character of fill_input
# result = CALL custom_ljust(text, width, fillchar)
# DISPLAY "Result: '[result]'"
# DISPLAY "Length: [length of result] characters"
# PROGRAM END


def custom_ljust(s, width, fillchar=' '):
    return s + fillchar * (width - len(s)) if len(s) < width else s

text = input("Enter text: ")
width = int(input("Enter width: "))
print(f"Result: '{custom_ljust(text, width)}'")