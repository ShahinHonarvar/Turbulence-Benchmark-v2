def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 3 or i >= 9 or (not '*' < c < 'E'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)