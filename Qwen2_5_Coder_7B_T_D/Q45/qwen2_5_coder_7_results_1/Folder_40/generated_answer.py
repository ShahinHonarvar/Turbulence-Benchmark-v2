def palindromes_between_indices(s):
    subset = s[4:10]
    subset = subset.lower()
    letters = set(subset)
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + 7, len(subset) + 1):
            word = ''.join(sorted(subset[i:j]))
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes