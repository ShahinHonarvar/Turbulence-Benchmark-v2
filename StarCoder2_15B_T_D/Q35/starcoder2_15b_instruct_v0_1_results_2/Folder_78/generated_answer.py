def remove_repeat_chars(s):
    char_counts = {}
    for i, c in enumerate(s):
        if i >= 62 and i < 96:
            char_counts[c] = char_counts.get(c, 0) + 1
    for c in set(s):
        if char_counts.get(c, 0) > 1:
            s = s.replace(c, '')
    return s