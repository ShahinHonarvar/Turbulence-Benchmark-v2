def remove_repeat_chars(s: str) -> str:
    """
    Removes repeated characters in a given string that occur between indices 355 and 988.
    """
    char_count = {}
    for c in s[355:988]:
        char_count[c] = char_count.get(c, 0) + 1
    result = []
    for c in s:
        if c not in char_count or char_count[c] == 1:
            result.append(c)
    return ''.join(result)