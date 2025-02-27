from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:8].lower()
    unique_chars = set(substring)
    palindromes = set()
    for perm in permutations(unique_chars, len(unique_chars)):
        perm_str = ''.join(perm)
        if perm_str == perm_str[::-1] and len(perm_str) >= 4:
            palindromes.add(perm_str)
    return palindromes