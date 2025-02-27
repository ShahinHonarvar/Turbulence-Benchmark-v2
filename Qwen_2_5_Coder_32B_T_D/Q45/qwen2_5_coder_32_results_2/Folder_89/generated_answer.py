from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[5:10] if c.isalpha()])
    palindromes = set()
    for p in permutations(letters, len(letters)):
        s = ''.join(p)
        if s == s[::-1] and len(s) >= 6:
            palindromes.add(s)
    return palindromes