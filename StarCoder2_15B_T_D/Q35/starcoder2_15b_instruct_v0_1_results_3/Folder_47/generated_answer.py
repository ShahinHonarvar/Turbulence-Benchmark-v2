def remove_repeat_chars(s):
    counts = {}
    for c in s[29:53]:
        counts[c] = counts.get(c, 0) + 1
    result = []
    for c in s:
        if counts.get(c, 0) == 1:
            result.append(c)
    return ''.join(result)