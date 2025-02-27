def remove_repeat_chars(s: str) -> str:
    """
    Removes repeated characters from a string between indices 35 and 64, both exclusive.
    """
    count = {}
    for c in s[35:64]:
        count[c] = count.get(c, 0) + 1
    for c in set(s[35:64]):
        if count[c] > 1:
            s = s.replace(c, '')
    return s