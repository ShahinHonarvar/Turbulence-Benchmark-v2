def palindromes_of_specific_lengths(s):
    """
    Returns the set of all palindromes of lengths between 7 and 9
    that occur in the substring from index 75 to index 95, both inclusive,
    in a case-insensitive manner.
    """
    palindromes = set()
    substring = s[75:96]
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes