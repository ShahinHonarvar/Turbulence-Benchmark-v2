def filter_chars(string):
    filtered_chars = []
    for i, c in enumerate(string):
        if i >= 35 and i < 60 and (not '!' < c < 'B'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)