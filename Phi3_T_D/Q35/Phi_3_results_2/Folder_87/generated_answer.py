def remove_repeat_chars(s):
    start, end = (20, 43)
    seen = set()
    result = []
    for i, c in enumerate(s):
        if i >= start and i < end:
            if c in seen:
                continue
            seen.add(c)
        result.append(c)
    return ''.join(result)