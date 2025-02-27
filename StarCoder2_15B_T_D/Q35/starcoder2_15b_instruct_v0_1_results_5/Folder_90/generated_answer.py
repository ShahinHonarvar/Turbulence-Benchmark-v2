def remove_repeat_chars(s):
    counts = {}
    for i, c in enumerate(s):
        if i >= 306 and i < 807:
            counts[c] = counts.get(c, 0) + 1
    for i, c in enumerate(s):
        if i >= 306 and i < 807 and (counts[c] > 1):
            s = s[:i] + s[i + 1:]
            counts[c] -= 1
    return s