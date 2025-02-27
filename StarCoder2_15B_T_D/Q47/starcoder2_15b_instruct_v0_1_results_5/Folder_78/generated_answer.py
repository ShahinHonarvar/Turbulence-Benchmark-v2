def palindromes_of_specific_lengths(string: str) -> set:
    """
    Finds all palindromes of specific lengths in a given string.
    """
    substring = string[15:73]
    palindromes = set()
    for length in range(19, 56):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes