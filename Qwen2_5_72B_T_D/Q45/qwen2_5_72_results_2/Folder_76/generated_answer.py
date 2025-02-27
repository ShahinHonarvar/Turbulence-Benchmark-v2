from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5]
    char_set = set(substring.lower())
    palindromes = set()
    for r in range(4, len(substring) + 1):
        for perm in permutations(substring.lower(), r):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return {p for p in palindromes if len(p) >= 4}