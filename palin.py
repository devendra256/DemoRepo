def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    for i in input_string:
        if i != " ":
            new_string += i
            reverse_string += i
    if new_string.lower() == reverse_string[::-1].lower():
        return True
    return False
print(is_palindrome("Never Odd or Even"))
print(is_palindrome("abc"))
print(is_palindrome("kavak"))
