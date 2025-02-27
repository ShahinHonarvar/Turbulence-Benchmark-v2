def filter_chars(text):
    filtered_chars = []
    for i, c in enumerate(text):
        if not (19 <= i <= 32 and 'f' <= c <= 'o'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)