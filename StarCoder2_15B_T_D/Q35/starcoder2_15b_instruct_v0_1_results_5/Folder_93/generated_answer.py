def remove_repeat_chars(s):
    char_counts = {}
    for c in s:
        char_counts[c] = char_counts.get(c, 0) + 1
    for c in char_counts:
        if char_counts[c] > 1 and 57 < s.index(c) < 85:
            s = s.replace(c, '')
    return s