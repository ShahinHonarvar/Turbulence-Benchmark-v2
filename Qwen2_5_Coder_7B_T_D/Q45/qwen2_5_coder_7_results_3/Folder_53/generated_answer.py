import itertools

def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for length in range(6, len(s) + 1):
        for perm in itertools.permutations(s, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes