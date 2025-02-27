from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7]
    s = s.lower()
    unique_chars = set(s)
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for perm in permutations(unique_chars, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes