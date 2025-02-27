def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 45 or i >= 57:
            filtered_chars.append(c)
        elif not 'F' < c < 'n':
            filtered_chars.append(c)
    return ''.join(filtered_chars)