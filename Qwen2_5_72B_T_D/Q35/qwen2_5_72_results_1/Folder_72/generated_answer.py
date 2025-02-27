def remove_repeat_chars(s):
    counts = {}
    for i in range(13, 70):
        if i < len(s):
            counts[s[i]] = counts.get(s[i], 0) + 1
    result = ''.join((c for i, c in enumerate(s) if i < 13 or i >= 70 or counts.get(c, 0) == 1))
    return result