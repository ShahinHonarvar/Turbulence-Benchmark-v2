def remove_repeat_chars(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in set(s):
        if counts[c] > 1 and 32 < ord(c) < 99:
            s = s.replace(c, '')
    return s