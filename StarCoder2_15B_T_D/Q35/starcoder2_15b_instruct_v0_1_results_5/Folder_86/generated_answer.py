def remove_repeat_chars(s: str) -> str:
    char_counts = {}
    for i, c in enumerate(s):
        if i >= 19 and i < 32:
            char_counts[c] = char_counts.get(c, 0) + 1
    for c in char_counts:
        if char_counts[c] > 1:
            s = s.replace(c, '')
    return s