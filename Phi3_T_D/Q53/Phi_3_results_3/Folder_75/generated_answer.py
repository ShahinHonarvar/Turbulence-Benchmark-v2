from itertools import combinations

def is_palindrome(s):
    return s.lower() == s[::-1].lower() and all((c.isalpha() for c in s))

def palindrome_of_length_at_least_n(s):
    result_set = set()
    for i in range(40, len(s) + 1):
        for start in range(len(s) - i + 1):
            substr = s[start:start + i]
            if is_palindrome(substr):
                result_set.add(substr.lower())
    return result_set