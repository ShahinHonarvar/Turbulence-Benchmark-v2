def filter_chars(s):
    filtered_chars = []
    for c in s:
        if c < 'S' or c > 's':
            filtered_chars.append(c)
    return ''.join(filtered_chars)