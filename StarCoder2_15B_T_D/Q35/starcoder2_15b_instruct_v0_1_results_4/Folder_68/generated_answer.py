def remove_repeat_chars(s):
    counts = dict()
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in counts:
        if counts[c] > 1 and c.isalpha():
            s = s.replace(c, '')
    return s