def is_palindrome(input_string):
    if input_string[::-1] == input_string:
        return True
    else:
        return False
print(is_palindrome("Never Odd or Even"))
print(is_palindrome("abc"))
print(is_palindrome("kavak"))
