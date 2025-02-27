from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:6].lower()
    seen = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            seen.add(candidate)
    return seen