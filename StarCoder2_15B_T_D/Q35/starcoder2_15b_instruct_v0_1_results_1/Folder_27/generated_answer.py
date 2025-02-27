def remove_repeat_chars(s):
    counts = {}
    for c in s[86:89]:
        counts[c] = s.count(c)
    for c, count in counts.items():
        if count > 1:
            s = s.replace(c, '')
    return s