def remove_repeat_chars(s):
    counts = {}
    for c in s[62:96]:
        counts[c] = counts.get(c, 0) + 1
    result = []
    for c in s:
        if counts[c] > 1:
            counts[c] -= 1
        else:
            result.append(c)
    return ''.join(result)