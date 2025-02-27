def remove_repeat_chars(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1 and 56 < s.index(c) < 90:
            s = s.replace(c, '')
    return s