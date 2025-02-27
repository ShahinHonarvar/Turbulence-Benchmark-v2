def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join(filter(lambda x: x in letters, s))
    palindromes = set()
    for i in range(len(s), 5, -1):
        for combination in set(itertools.permutations(s, i)):
            candidate = ''.join(combination)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes