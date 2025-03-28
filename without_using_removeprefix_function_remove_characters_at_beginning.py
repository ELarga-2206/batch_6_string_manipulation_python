#removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

def removeprefix(s, prefix):
     if s.startswith(prefix):
         return s[len(prefix):]
     return s
 
main_string = input("Enter the string: ")
prefix = input("Enter the prefix to remove: ")
 
result = removeprefix(main_string, prefix)
print("\nResult after removing prefix:")
print(result)