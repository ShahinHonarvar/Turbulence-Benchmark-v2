def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 35 or i >= 60 or (not '!' < c < 'B'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)