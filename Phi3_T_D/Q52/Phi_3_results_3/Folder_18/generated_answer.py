from itertools import product

def is_palindrome(substring):
    return substring == substring[::-1] and all(('a' <= c <= 'z' for c in substring))

def palindrome_of_length_n(s):
    s_lower = s.lower()
    ret_set = set()
    for i in range(len(s_lower) - 391):
        substring = s_lower[i:i + 392]
        if is_palindrome(substring):
            ret_set.add(substring.upper())
    return ret_set