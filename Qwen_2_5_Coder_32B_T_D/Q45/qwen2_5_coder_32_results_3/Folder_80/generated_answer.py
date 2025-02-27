from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 7):
        p = ''.join(perm)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes