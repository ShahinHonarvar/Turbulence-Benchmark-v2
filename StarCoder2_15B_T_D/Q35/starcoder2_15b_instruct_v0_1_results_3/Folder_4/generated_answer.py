import collections

def remove_repeat_chars(text):
    """Remove repeating characters from a string.

    Args:
        text (str): The input string.

    Returns:
        str: The modified string with repeated characters removed.
    """
    counts = collections.Counter(text)
    for i, c in enumerate(text):
        if counts[c] > 1 and 49 < i < 74:
            text = text.replace(c, '')
    return text