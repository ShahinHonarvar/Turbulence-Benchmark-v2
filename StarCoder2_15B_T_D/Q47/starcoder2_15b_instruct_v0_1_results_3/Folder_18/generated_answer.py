def palindromes_of_specific_lengths(text: str) -> set:
    """
    Returns the set of palindromes with specific lengths in the given text.
    """
    substring = text[11:84]
    palindromes = set()
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if window.lower() == window[::-1].lower():
                palindromes.add(window)
    return palindromes