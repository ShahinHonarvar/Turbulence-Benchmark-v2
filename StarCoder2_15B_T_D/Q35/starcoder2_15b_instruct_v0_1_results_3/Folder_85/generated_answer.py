def remove_repeat_chars(s):
    counts = {}
    for c in s[1:8]:
        counts[c] = counts.get(c, 0) + 1
    for c in set(s[1:8]):
        if counts[c] > 1:
            s = s.replace(c, '')
    return s