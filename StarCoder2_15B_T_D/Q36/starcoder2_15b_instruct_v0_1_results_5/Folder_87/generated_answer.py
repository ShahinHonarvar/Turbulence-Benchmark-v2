def filter_chars(s):
    filtered_chars = []
    for c in s:
        if c < '3' or c > 'D':
            filtered_chars.append(c)
    return ''.join(filtered_chars)