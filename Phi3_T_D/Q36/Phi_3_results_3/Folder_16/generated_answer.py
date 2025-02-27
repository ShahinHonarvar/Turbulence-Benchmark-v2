def filter_chars(s):
    result = list(s)
    for i in range(331, 713):
        if 'M' < result[i] < '_':
            result[i:] = [c for c in result[i:] if c != result[i]]
    return ''.join(result)