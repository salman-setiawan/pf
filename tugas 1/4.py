test = "rotator"

def is_palindrome(text):
    return "True" if text == text[::-1] else "False"

print(is_palindrome(test))