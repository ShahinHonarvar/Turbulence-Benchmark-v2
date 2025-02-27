def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = set(s)
    palindromes = set()
    for length in range(4, len(s) + 1):
        for perm in set(permutations(letters, length)):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes