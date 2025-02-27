def palindromes_between_indices(s):
    subset = s[4:10]
    subset = subset.lower()
    subset = ''.join(filter(str.isalpha, subset))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for length in range(3, len(subset) + 1):
        for perm in permutations(alphabet, length):
            perm_str = ''.join(perm)
            if perm_str in subset and perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes