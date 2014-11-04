"""returns True if my_string is a palindrome, else False"""

def is_palindrome(my_string):
    """returns True if my_string is a palindrome, else False"""
    for i, j in zip(my_string, my_string[::-1]):
        if i != j:
            return False
    return True
