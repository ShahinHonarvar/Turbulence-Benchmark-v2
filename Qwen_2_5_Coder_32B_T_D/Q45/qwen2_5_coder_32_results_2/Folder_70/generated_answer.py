from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:7] if c.lower() in ascii_lowercase))
    seen = set()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes