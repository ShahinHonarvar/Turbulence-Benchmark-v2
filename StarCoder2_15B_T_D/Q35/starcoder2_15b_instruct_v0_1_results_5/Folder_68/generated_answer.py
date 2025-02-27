def remove_repeat_chars(s):
    char_counts = {}
    for c in s:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    for c in char_counts:
        if char_counts[c] > 1:
            s = s.replace(c, '')
    return s