def palindromes_between_indices(s):
    subset = s[3:10]
    subset = subset.lower()
    letters = set(subset)
    length = 5
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + length, len(subset) + 1):
            sub = subset[i:j]
            if sub == sub[::-1]:
                for p in permutations(sub):
                    palindromes.add(''.join(p))
    return palindromes