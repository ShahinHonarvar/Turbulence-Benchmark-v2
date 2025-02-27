def remove_repeat_chars(s):
    """
    Removes all occurrences of characters repeated between indices 20 to 36 from a string.

    Args:
    s (str): Input string.

    Returns:
    str: Altered string without the specified characters.
    """
    target_chars = set()
    idx_start, idx_end = (20, 36)
    for idx, char in enumerate(s[idx_start:idx_end]):
        if s.count(char, idx_start, idx_end) > 1:
            target_chars.add(char)
    return ''.join((char for char in s if char not in target_chars))