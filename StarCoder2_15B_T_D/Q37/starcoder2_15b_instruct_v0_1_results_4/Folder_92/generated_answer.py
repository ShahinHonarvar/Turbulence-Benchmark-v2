def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if not (4 <= i <= 4 and '7' <= c <= 'o'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)