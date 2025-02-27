from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(text):
    substring = text[1:5].lower()
    unique_chars = set(substring)
    palindromes = set()
    for i in range(3, len(substring) + 1, 2):
        for perm in permutations(unique_chars, i):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes