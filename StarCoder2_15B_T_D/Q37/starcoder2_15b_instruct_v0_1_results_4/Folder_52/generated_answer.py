def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if not (54 <= i <= 83 and 'j' <= c <= 'v'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)