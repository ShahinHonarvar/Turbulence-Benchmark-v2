def filter_chars(s):
    filtered_chars = []
    for c in s:
        if c < 'F' or c > 'n':
            filtered_chars.append(c)
    return ''.join(filtered_chars)