def palindromes_between_indices(s):
    s = s[6:9].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s), 2, -1):
        for perm in permutations(s, i):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1] and all((char in letters for char in perm_str)):
                palindromes.add(perm_str)
    return palindromes