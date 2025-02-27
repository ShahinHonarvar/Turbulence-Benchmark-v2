from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    chars = set(s)
    palindromes = set()
    for r in range(4, len(chars) + 1):
        for perm in permutations(chars, r):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes