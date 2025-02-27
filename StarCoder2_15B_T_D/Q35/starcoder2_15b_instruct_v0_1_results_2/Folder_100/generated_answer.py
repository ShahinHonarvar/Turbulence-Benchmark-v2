def remove_repeat_chars(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for i, c in enumerate(s):
        if counts[c] > 1 and 44 < i < 78:
            s = s.replace(c, '')
            counts[c] = 0
    return s