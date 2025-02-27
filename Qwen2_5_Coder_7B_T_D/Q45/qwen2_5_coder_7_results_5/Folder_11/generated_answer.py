from itertools import permutations

def palindromes_between_indices(s):
    range_str = s[3:8]
    length = len(range_str)
    unique_chars = ''.join(sorted(set(range_str.lower())))
    palindromes = set()
    for perm in permutations(unique_chars, length):
        perm_str = ''.join(perm)
        if perm_str.lower() == perm_str[::-1].lower() and length >= 4:
            palindromes.add(perm_str)
    return palindromes