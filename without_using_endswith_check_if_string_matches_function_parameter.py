# endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

def ends(main, suffix):
    return len(main) >= len(suffix) and main[-len(suffix):] == suffix
    
main = input("Main string: ")
suffix = input("check if ends with: ")
print("Ends with!" if ends(main, suffix) else "Doesn't end with")