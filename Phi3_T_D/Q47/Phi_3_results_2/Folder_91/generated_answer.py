import string

def is_valid_char(c):
    return c in string.ascii_letters

def is_palindrome(s, start, end):
    while start < end:
        if not is_valid_char(s[start]) or not is_valid_char(s[end]):
            return False
        if s[start].lower() != s[end].lower():
            return False
        start, end = (start + 1, end - 1)
    return True

def palindromes_of_specific_lengths(s):
    result = set()
    length = len(s)
    for window_size in range(3, 6):
        for i in range(length - window_size + 1):
            if i > 10:
                break
            if is_palindrome(s, i, i + window_size - 1):
                result.add(s[i:i + window_size])
    return result