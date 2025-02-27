from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, min(8, len(letters))):
        p = ''.join(perm)
        if len(p) >= 6 and p == p[::-1]:
            palindromes.add(p)
    return palindromes