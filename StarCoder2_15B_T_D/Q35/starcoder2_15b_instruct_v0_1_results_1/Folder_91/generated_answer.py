def remove_repeat_chars(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1 and s.index(c) >= 0 and (s.index(c) < 6):
            s = s.replace(c, '')
    return s