def remove_repeat_chars(s):
    """
    Removes repeated characters from a string.
    """
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    for c in set(s):
        if char_counts[c] > 1 and 0 < s.index(c) < 10:
            s = s.replace(c, '')
    return s