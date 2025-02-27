def remove_repeat_chars(s):
    counts = {}
    for c in s[34:69]:
        counts[c] = counts.get(c, 0) + 1
    for c, count in counts.items():
        if count > 1:
            s = s.replace(c, '')
    return s