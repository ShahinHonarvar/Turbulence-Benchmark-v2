def remove_repeat_chars(s):
    start, end = (57, 85)
    seen = set()
    result = []
    for i, c in enumerate(s):
        if start <= i < end:
            if c in seen:
                continue
            elif s[i + 1:end].count(c) > 0:
                seen.add(c)
            else:
                result.append(c)
        else:
            result.append(c)
    return ''.join(result)