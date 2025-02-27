def palindromes_between_indices(s):
    subset = s[5:10]
    subset = subset.lower()
    unique_chars = set(subset)
    palindromes = set()
    for length in range(4, 11):
        for char_tuple in set(itertools.permutations(unique_chars, length)):
            char_tuple = ''.join(char_tuple)
            if char_tuple == char_tuple[::-1]:
                palindromes.add(char_tuple)
    return palindromes