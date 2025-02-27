def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 55 or i >= 80 or (not 'S' < c < 's'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)