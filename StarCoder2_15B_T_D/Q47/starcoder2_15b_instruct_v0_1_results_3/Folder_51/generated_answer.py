def palindromes_of_specific_lengths(string: str) -> set:
    """
    Finds palindromes of specific lengths in a given string.

    Args:
        string (str): The input string.

    Returns:
        set: A set of palindromes of specific lengths.
    """
    palindromes = set()
    lower_string = string.lower()
    substring = lower_string[2:9]
    for i in range(len(substring) - 2):
        for length in range(3, 5):
            window = substring[i:i + length]
            if window == window[::-1]:
                palindromes.add(window)
    return palindromes