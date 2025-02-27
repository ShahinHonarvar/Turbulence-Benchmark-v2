from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    seen = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            seen.add(candidate)
    return seen