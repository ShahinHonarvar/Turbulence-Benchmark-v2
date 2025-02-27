from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[1:5] if c.isalpha()])
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if len(p) >= 4 and p == p[::-1]:
            palindromes.add(p)
    return palindromes