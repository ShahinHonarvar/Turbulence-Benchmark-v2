def palindromes_between_indices(string):
    """
    This function takes a string as an argument and returns a set of all palindromes
    of the length of at least 4 such that each palindrome is created from any possible
    arrangement of the English letters in the given string that occur between index 2
    to index 4, both inclusive. If no such palindromes of the specified length can be
    created from the English letters of the given string that occur in the specified range,
    the function returns an empty set.
    """
    filtered_string = ''.join((c for c in string if c.isalpha()))
    palindromes = set()
    for i in range(len(filtered_string) - 3):
        for j in range(i + 3, len(filtered_string)):
            substring = filtered_string[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes