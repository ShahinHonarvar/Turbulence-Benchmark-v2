def remove_repeat_chars(s):
    counts = {}
    for i, c in enumerate(s):
        if 36 < i < 52:
            counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1:
            s = s.replace(c, '')
    return s