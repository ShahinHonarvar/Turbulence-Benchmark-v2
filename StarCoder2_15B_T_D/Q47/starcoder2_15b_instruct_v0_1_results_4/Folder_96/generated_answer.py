def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes of lengths between 50 and 100 (both inclusive)
    that occur in the substring of `string` from index 100 to index 300 (both inclusive).
    """
    substring = string[100:301]
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes