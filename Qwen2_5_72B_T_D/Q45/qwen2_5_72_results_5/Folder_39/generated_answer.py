from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    unique_chars = set(substring)
    if len(unique_chars) < 2:
        return set()
    palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            palindromes.add(candidate)
    return palindromes