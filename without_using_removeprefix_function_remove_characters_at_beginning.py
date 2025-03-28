#removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#FUNCTION custom_removeprefix(s, prefix):
# IF string 's' starts with 'prefix':
# RETURN substring of 's' starting after 'prefix'
# ELSE:
# RETURN original string 's'

def removeprefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]
    return s

main_string = input("Enter the string: ")
prefix = input("Enter the prefix to remove: ")

result = removeprefix(main_string, prefix)
print("\nResult after removing prefix:")
print(result)
