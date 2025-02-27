from itertools import combinations

def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    all_substrings = {s[start:end] for start in range(len(s)) for end in range(start + 1, len(s) + 1)}
    possible_palindromes = {substr for substr in all_substrings if all((c.isalpha() for c in substr)) and len(substr) >= 137 and is_palindrome(substr)}
    return {substr.lower() for substr in possible_palindromes}