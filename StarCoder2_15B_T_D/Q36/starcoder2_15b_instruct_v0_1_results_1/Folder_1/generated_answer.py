def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 69 or i >= 87 or c <= '#' or (c >= 'L'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)