import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    palindromes = set()
    for perm in set(itertools.permutations(letters, len(letters))):
        mid = len(perm) // 2
        if perm[:mid] == perm[-(mid - (1 - len(perm) % 2)):-1] and len(perm) >= 5:
            palindromes.add(''.join(perm))
    return palindromes