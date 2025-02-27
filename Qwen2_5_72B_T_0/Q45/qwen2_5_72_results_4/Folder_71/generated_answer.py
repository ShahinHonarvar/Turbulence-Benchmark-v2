from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:4].lower()
    unique_chars = set(substring)
    palindromes = set()
    for r in range(2, len(substring) + 1):
        for perm in permutations(unique_chars, r):
            candidate = ''.join(perm)
            if candidate == candidate[::-1] and len(candidate) >= 4:
                palindromes.add(candidate)
    return palindromes