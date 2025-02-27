def remove_repeat_chars(s):
    char_counts = {}
    for i, c in enumerate(s):
        if 70 < i < 200:
            char_counts[c] = char_counts.get(c, 0) + 1
    for c in char_counts:
        if char_counts[c] > 1:
            s = ''.join([x for x in s if x != c])
    return s