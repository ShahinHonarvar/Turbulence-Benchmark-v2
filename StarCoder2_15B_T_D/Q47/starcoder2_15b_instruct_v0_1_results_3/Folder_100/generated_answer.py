def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes of specific lengths in a given string.
    Only palindromes of lengths between 12 and 18 (both inclusive) are considered.
    Only palindromes occurring in the substring from index 29 to index 96, both inclusive, are considered.
    Palindromes should only consist of English letters.
    The matching should be case-insensitive.
    """
    palindromes = set()
    substring = string[29:97]
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1] and window.isalpha():
                palindromes.add(window)
    return palindromes