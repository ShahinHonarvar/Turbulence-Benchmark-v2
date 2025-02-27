def remove_repeat_chars(s):
    counts = {}
    for c in s[0:4]:
        counts[c] = counts.get(c, 0) + 1
    for c in list(s):
        if c in counts and counts[c] > 1:
            s = s.replace(c, '')
    return s