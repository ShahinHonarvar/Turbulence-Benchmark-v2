def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 31 or i >= 73 or (not 'M' < c < 'j'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)