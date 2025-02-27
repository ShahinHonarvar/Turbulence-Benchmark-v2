from itertools import permutations

def palindromes_between_indices(s):
    mid = s[5:8].lower()
    palindromes = set()
    for perm in permutations(mid):
        candidate = ''.join(perm) + ''.join(reversed(perm))
        if len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes