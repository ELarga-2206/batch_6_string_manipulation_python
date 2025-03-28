#lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

#FUNCTION to_lowercase(s):
    #CREATE empty result string
    #FOR each character in input string s:
        #GET ASCII value of character
        #IF character is uppercase (A-Z):
            #CONVERT to lowercase by adding 32 to ASCII value
            #ADD converted character to result
        #ELSE:
            #ADD character to result unchanged
    #RETURN result

def to_lowercase(s):
    result = []
    for char in s:
        if 65 < ord(char) < 90:
            result.append((char) + 32)
        else:
            result.append(char)