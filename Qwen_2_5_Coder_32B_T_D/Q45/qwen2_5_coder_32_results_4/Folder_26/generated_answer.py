from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:7] if c.isalpha()]
    letters = letters + [c.lower() for c in letters if c.isupper()] + [c.upper() for c in letters if c.islower()]
    palindromes = set()
    for perm in permutations(letters, 3):
        p = ''.join(perm)
        if p.lower() == p[::-1].lower():
            palindromes.add(p.lower())
    return palindromes