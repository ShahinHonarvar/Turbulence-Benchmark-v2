def remove_repeat_chars(s):
    start, end = (57, 84)
    skip_chars = set()
    result = []
    for i in range(len(s)):
        if i >= start and i < end:
            if s[i] in skip_chars:
                continue
            if s.count(s[i], i, end) > 1:
                skip_chars.add(s[i])
                continue
        result.append(s[i])
    return ''.join(result)