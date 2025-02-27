def remove_repeat_chars(s):
    indices = range(46, 91)
    seen = set()
    result = []
    for i, c in enumerate(s):
        if 46 < i < 91:
            if c not in seen:
                seen.add(c)
            else:
                continue
        result.append(c)
    return ''.join(result)