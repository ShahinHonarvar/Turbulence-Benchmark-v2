def filter_chars(s):
    result = []
    for i, c in enumerate(s[11:32]):
        if '!' <= c <= '@':
            continue
        result.append(s[i])
    return ''.join(result)