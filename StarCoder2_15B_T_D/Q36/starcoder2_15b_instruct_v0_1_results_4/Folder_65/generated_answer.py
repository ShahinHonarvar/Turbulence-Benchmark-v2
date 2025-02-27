def filter_chars(s):
    filtered = []
    for c in s:
        if c <= 'F' or c >= 'O':
            filtered.append(c)
    return ''.join(filtered)