def remove_repeat_chars(s: str) -> str:
    """
    Removes repeated characters in a string between indices 46 and 91.
    """
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    to_remove = []
    for c, count in char_counts.items():
        if count > 1 and 46 < ord(c) < 91:
            to_remove.append(c)
    return ''.join([c for c in s if c not in to_remove])