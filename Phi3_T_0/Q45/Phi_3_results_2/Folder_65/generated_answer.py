from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s if c.isalpha()][:7]
    palindromes = set()
    for i in range(5, 8):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes