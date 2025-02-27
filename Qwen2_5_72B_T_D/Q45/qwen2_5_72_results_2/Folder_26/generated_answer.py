from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:7].lower()
    unique_chars = set(substring)
    if len(unique_chars) < 2:
        return set()
    palindromes = set()
    for perm in permutations(unique_chars, 3):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes