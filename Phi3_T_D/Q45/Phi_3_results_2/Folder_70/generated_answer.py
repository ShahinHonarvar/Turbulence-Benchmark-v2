from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    substring = s[1:7].lower()
    chars = set(substring)
    valid_palindromes = set()
    for length in range(4, len(substring) + 1):
        for p in permutations(chars, length):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes