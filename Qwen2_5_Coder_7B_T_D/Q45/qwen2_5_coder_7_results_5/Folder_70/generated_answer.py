from itertools import permutations
    import string

def palindromes_between_indices(s):
    s = s[1:7].lower()
    chars = list(s)
    palindromes = set()
    for length in range(4, len(chars) + 1):
        for perm in permutations(chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes