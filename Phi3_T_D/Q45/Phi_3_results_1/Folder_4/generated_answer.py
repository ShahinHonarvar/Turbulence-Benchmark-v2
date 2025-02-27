from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    unique_chars = set(substring)
    potential_palindromes = set()
    for n in range(7, len(substring) + 1):
        for perm in permutations(substring, n):
            potential_palindromes.add(''.join(perm))
    return {p for p in potential_palindromes if is_palindrome(p)}