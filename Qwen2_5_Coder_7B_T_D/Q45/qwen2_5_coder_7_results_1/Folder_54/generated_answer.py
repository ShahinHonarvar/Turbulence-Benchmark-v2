def palindromes_between_indices(s):
    subset = s[4:10]
    subset = subset.lower()
    unique_chars = set(subset)
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + 3, len(subset) + 1):
            for chars in set(permutations(subset[i:j])):
                if chars == chars[::-1]:
                    palindromes.add(''.join(chars))
    return palindromes