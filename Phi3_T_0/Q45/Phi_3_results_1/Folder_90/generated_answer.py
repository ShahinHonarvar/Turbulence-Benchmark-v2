from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s if c.isalpha()][:6]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for perm in permutations(letters, i):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes