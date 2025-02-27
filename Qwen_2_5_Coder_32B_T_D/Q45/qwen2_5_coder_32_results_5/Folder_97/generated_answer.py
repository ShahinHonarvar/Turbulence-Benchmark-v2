from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s[:5].lower()
    letters = ''.join([c for c in s if c in ascii_lowercase])
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            cand = ''.join(perm)
            if cand == cand[::-1]:
                palindromes.add(cand)
    return palindromes