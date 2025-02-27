def remove_repeat_chars(s):
    counts = {}
    for i, c in enumerate(s):
        if i >= 409 and i < 502:
            counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1:
            s = s.replace(c, '')
    return s