def remove_repeat_chars(s: str) -> str:
    """
    Removes repeated characters in a given string within a specific index range.
    """
    frequencies = {}
    for c in s[36:52]:
        frequencies[c] = frequencies.get(c, 0) + 1
    for c in set(s[36:52]):
        if frequencies[c] > 1:
            s = s.replace(c, '')
    return s