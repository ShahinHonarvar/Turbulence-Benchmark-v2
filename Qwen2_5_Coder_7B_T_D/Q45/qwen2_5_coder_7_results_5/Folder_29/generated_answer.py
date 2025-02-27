def palindromes_between_indices(s):
    s = s[2:10]
    s = s.lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters), 6, -1):
        for combination in itertools.permutations(letters, i):
            candidate = ''.join(combination)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes