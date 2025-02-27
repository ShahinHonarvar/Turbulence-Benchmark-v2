def filter_chars(text):
    filtered_chars = []
    for c in text:
        if c < 'i' or c > 'v':
            filtered_chars.append(c)
    return ''.join(filtered_chars)