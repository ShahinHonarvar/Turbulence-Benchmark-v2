def remove_repeat_chars(s):
    counts = {}
    for i, c in enumerate(s):
        if i >= 7 and i < len(s) - 1:
            counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1:
            s = s.replace(c, '')
    return s