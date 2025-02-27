def remove_repeat_chars(s: str) -> str:
    """
    Removes repeated characters in a string within a given character count range.
    """
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1 and 43 < ord(char) < 70:
            s = s.replace(char, '')
    return s