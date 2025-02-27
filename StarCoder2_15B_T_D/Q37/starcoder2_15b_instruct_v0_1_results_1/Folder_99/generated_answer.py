def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if not (373 <= i <= 901 and 'T' <= c <= 'h'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)