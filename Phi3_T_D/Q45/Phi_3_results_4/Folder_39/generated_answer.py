from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    unique_chars = set(substring)
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(unique_chars, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes