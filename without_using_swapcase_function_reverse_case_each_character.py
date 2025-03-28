#swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

#PROGRAM START:
# DISPLAY "Enter a string to swap cases:"
# GET input from user
# swapped_output = CALL swap(user_input)
# DISPLAY "Case-swapped result:"
# DISPLAY swapped_output
# PROGRAM END 

#FUNCTION custom_swapcase(s):
    #CREATE empty result string
    #FOR each character in input string s:
        #IF character is uppercase:
            #CONVERT to lowercase and ADD to result
        #ELSE IF character is lowercase:
            #CONVERT to uppercase and ADD to result
        #ELSE:
            #ADD character to result unchanged
    #RETURN the result

swapcase = () 
swapped_output = ()
user_input = input("Enter a string to swap cases: ")

swapped_output = swapcase(user_input)
print("\nCase-swapped result:")
print(swapped_output)