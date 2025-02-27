def filter_chars(text):
    filtered_chars = []
    for i, c in enumerate(text):
        if i < 27 or i >= 75 or (not 'A' < c < 'i'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)