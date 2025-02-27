def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 154 or i >= 222 or c <= 'A' or (c >= 'f'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)