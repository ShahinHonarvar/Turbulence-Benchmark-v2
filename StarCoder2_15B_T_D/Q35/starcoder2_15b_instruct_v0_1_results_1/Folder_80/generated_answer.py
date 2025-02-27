def remove_repeat_chars(s):
    counts = {}
    for i, c in enumerate(s):
        if i >= 57 and i < 84:
            counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1:
            s = s.replace(c, '')
    return s