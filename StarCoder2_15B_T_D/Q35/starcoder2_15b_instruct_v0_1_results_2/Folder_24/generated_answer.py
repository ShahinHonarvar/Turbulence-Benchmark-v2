def remove_repeat_chars(s):
    char_counts = {}
    for i, c in enumerate(s):
        if i > 13 and i < 91:
            char_counts[c] = char_counts.get(c, 0) + 1
    for c, count in char_counts.items():
        if count > 1:
            s = s.replace(c, '')
    return s