def remove_repeat_chars(s):
    counts = {}
    for i in range(5):
        counts[s[i]] = counts.get(s[i], 0) + 1
    return ''.join((c for i, c in enumerate(s) if counts.get(c, 0) <= 1 or i > 5))