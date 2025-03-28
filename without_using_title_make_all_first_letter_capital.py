#title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

#PROGRAM START
    # DISPLAY "Enter a sentence to convert to title case:"
    # GET input from user
    # output = CALL simple_title(user_input) 
    # DISPLAY title_case_output

def simple_title(s):
    return ' '.join(w.capitalize() for w in s.split())