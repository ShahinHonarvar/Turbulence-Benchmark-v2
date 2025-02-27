def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

def get_all_substrings(string):
    length = len(string)
    return [string[i:j] for i in range(length) for j in range(i + 1, length + 1)]

def palindrome_of_length_n(s):
    return {substr.lower() for substr in get_all_substrings(s) if len(substr) == 276 and substr.isalpha() and is_palindrome(substr)}