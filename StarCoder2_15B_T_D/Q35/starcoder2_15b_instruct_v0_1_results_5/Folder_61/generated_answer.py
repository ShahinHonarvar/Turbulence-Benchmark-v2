def remove_repeat_chars(string):
    seen = {}
    result = []
    for c in string:
        if c not in seen:
            seen[c] = 0
        seen[c] += 1
    for c in string:
        if seen[c] > 1 and 0 < string.index(c) < 8:
            continue
        result.append(c)
    return ''.join(result)