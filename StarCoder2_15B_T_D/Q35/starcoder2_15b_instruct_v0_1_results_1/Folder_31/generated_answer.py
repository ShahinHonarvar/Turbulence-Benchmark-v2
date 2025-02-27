def remove_repeat_chars(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1 and 33 < s.index(c) < 78:
            s = s.replace(c, '')
    return s