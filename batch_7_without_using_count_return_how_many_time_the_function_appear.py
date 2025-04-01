# count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

def custom_count(text, substring):
    count = 0
    sub_len = len(substring)
    for i in range(len(text) - sub_len + 1):
        if text[i:i+sub_len] == substring:
            count += 1

    return count

user_text = input("Enter the main text: ")
user_sub = input("Enter the substring to count: ")

result = custom_count(user_text, user_sub)
print(f"The substring appears {result} times")