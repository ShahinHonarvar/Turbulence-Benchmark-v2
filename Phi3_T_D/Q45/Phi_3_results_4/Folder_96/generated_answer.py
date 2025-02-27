from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = sorted(set(s.lower())[3:9])
    palindromes = set()
    if len(letters) < 6:
        return palindromes
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm).lower())
    return palindromes