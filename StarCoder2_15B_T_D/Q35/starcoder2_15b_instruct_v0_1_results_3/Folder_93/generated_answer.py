def remove_repeat_chars(s):
    counts = {}
    for c in s[57:85]:
        counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1:
            s = s.replace(c, '')
    return s