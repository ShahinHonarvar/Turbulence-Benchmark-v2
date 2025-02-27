from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    found_palindromes = set()
    for start in range(len(text)):
        for end in range(start + 72, len(text) + 1):
            substring = text[start:end]
            if set(substring).issubset(valid_chars) and is_palindrome(substring):
                found_palindromes.add(substring)
    return found_palindromes