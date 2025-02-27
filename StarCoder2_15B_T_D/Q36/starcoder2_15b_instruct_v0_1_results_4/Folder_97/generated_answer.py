def filter_chars(text):
    filtered_chars = []
    for i, c in enumerate(text):
        if i < 309 or i >= 591:
            filtered_chars.append(c)
        elif c <= 'S' or c >= 'm':
            filtered_chars.append(c)
    return ''.join(filtered_chars)