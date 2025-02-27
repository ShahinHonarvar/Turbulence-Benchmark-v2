from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6].lower()
    unique_chars = set(substring)
    palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes