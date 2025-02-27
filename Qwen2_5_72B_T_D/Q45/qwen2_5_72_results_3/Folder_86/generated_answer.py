from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    unique_chars = set(substring)
    palindromes = set()
    for perm in permutations(unique_chars, len(unique_chars)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            palindromes.add(candidate)
    return palindromes