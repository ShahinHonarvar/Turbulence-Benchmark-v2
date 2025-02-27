def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 15 or i >= 85 or (not 'I' < c < 'M'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)