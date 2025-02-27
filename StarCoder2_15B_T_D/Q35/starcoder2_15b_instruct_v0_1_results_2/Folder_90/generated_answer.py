def remove_repeat_chars(s):
    char_counts = {}
    for i, c in enumerate(s):
        if c not in char_counts:
            char_counts[c] = []
        char_counts[c].append(i)
    for c, indices in char_counts.items():
        if len(indices) > 1 and 306 < indices[0] < 807:
            s = s.replace(c, '')
    return s