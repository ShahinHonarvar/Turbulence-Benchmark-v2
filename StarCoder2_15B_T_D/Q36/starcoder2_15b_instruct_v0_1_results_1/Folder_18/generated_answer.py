def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if not (587 < i < 648 and ',' < c < 'c'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)