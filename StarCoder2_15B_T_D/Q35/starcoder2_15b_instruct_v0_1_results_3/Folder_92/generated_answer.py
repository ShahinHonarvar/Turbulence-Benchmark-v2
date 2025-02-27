def remove_repeat_chars(string: str) -> str:
    """
    Removes repeated characters from a string.

    Args:
        string: The input string.

    Returns:
        The modified string with repeated characters removed.
    """
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in char_counts:
        if char_counts[char] > 1:
            string = string.replace(char, '')
    return string