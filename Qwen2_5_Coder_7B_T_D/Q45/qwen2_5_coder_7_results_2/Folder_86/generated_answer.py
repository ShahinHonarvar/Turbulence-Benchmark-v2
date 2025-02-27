def palindromes_between_indices(s):
    subset = s[6:10].lower()
    unique_chars = set(subset)
    palindromes = set()
    for i in range(len(unique_chars), 4, -1):
        for chars in itertools.permutations(unique_chars, i):
            candidate = ''.join(chars)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes