def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if 1 <= i < 6 and ',' < c < 'f' or (i < 1 or i >= 6):
            filtered_chars.append(c)
    return ''.join(filtered_chars)