def filter_chars(s):
    filtered_chars = []
    for c in s:
        if c < 'E' or c > '~':
            continue
        if not 63 <= ord(c) <= 84:
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)