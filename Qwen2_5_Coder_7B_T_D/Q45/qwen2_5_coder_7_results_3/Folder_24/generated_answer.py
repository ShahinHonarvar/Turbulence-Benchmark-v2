from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = set(s)
    palindromes = set()
    for i in range(4, len(s) + 1):
        for perm in permutations(letters, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes