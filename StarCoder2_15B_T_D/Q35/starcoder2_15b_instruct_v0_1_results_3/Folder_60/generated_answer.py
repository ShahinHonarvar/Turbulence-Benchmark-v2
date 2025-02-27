def remove_repeat_chars(s):
    char_counts = {}
    for i, c in enumerate(s):
        if i < 38 or i >= 52:
            continue
        char_counts[c] = char_counts.get(c, 0) + 1
    for c in char_counts:
        if char_counts[c] > 1:
            s = s.replace(c, '')
    return s