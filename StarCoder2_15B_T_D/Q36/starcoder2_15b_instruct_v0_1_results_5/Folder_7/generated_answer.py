def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 502 or i >= 946 or c <= 'W' or (c >= 'y'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)