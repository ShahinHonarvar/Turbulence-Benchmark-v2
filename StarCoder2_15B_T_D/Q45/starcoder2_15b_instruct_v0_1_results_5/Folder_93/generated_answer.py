def palindromes_between_indices(string):
    """Return a set of palindromes of length at least 6 that can be formed from any possible arrangement of English letters in the given string that occur between indices 2 and 7, both inclusive."""
    string = string.lower()
    palindromes = set()
    for i in range(2, len(string) - 4):
        for j in range(i + 6, len(string)):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes