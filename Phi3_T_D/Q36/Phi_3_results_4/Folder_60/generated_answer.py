def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if 23 < i < 83 and 'f' < c < 'o':
            continue
        result += c
    return result