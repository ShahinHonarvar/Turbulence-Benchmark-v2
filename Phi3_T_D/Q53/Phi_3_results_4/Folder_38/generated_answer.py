from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    result_set = set()
    text = text.lower()
    length = 56
    for start_index in range(len(text) - length + 1):
        substr = text[start_index:start_index + length]
        if all((char.isalpha() for char in substr)):
            if is_palindrome(substr):
                result_set.add(substr.upper())
    return result_set