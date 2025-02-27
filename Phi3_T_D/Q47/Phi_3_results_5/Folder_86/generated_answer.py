def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

def is_valid_char(char):
    return 'a' <= char <= 'z'

def palindromes_of_specific_lengths(s):
    start, end = (30, 95)
    return {s[i:j + 1].lower() for i in range(start, end + 1) for j in range(i + 33, min(i + 56, end)) if all((is_valid_char(c) for c in s[i:j + 1])) and is_palindrome(s[i:j + 1])}