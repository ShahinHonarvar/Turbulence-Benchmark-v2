def filter_chars(s):
    filtered = []
    for c in s:
        if c < 'P' or c > 'x':
            filtered.append(c)
    return ''.join(filtered)