def remove_repeat_chars(s):
    char_counts = {}
    for i, c in enumerate(s):
        if i < 3 or i >= 8:
            continue
        if c not in char_counts:
            char_counts[c] = 0
        char_counts[c] += 1
    for c in char_counts:
        if char_counts[c] > 1:
            s = s.replace(c, '')
    return s