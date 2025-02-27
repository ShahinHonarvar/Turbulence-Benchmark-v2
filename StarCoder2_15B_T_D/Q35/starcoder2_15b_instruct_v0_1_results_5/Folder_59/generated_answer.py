def remove_repeat_chars(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    result = []
    for c in s:
        if counts[c] == 1 or s.index(c) < 10:
            result.append(c)
    return ''.join(result)