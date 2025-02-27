def remove_repeat_chars(s: str) -> str:
    char_counts = {}
    for i, c in enumerate(s):
        if i >= 25 and i < 80:
            char_counts[c] = char_counts.get(c, 0) + 1
    for c, count in char_counts.items():
        if count > 1:
            s = s.replace(c, '')
    return s