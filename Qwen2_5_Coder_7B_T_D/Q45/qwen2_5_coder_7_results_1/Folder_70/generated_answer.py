def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = sorted(set(s))
    max_length = len(letters)
    palindromes = set()
    for length in range(4, max_length + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if perm_str == perm_str[::-1]:
                palindromes.add(perm_str)
    return palindromes