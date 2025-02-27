from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, min(3, len(letters))):
        p = ''.join(perm)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes