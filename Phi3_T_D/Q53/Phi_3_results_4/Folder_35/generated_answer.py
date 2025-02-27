from itertools import combinations

def is_palindrome(s):
    return s.upper() == s.upper()[::-1]

def palindrome_of_length_at_least_n(text):
    letters = ''.join([char for char in text.lower() if char.isalpha()])
    result = set()
    for length in range(26, len(letters) + 1):
        for start in range(len(letters) - length + 1):
            candidate = letters[start:start + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result