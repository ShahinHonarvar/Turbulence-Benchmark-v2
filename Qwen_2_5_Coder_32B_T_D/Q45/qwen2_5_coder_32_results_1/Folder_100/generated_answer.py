import itertools

def palindromes_between_indices(s):
    letters = ''.join(sorted([c.lower() for c in s[:6] if c.isalpha()]))
    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            palindromes.add(perm_str)
    return palindromes