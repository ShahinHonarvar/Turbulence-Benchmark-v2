def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s), 2, -1):
        for comb in itertools.permutations(s, i):
            word = ''.join(comb)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes