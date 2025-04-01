# removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

def custom_removesuffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text