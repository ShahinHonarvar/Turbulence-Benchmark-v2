from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string_lower = string.lower()
    for i in range(len(string_lower) - 85):
        for j in range(92, len(string_lower) - i + 1):
            substr = string_lower[i:j]
            if all((c.isalpha() for c in substr)) and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes