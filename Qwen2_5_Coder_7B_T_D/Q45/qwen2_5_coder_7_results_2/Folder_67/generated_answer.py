from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    chars = ''.join(sorted(s))
    unique_chars = ''.join(dict.fromkeys(chars))
    palindromes = set()
    for r in range(5, len(unique_chars) + 1):
        for perm in permutations(unique_chars, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes