def remove_repeat_chars(s):
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    for c, count in char_counts.items():
        if count > 1 and s.index(c) < 2:
            s = s.replace(c, '')
    return s