def remove_repeat_chars(text):
    """Remove repeat characters from a string.

    Args:
        text (str): The input string.

    Returns:
        str: The modified string with repeated characters removed.
    """
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = [char for char, count in char_counts.items() if count > 1 and char != text[0] and (char != text[-1])]
    for char in repeated_chars:
        text = text.replace(char, '')
    return text