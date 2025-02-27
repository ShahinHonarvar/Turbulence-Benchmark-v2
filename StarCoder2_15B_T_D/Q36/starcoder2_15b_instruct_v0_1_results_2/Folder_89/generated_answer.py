def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i >= 57 and i < 69 and ('(' < c < 'W'):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)