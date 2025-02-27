def filter_chars(s):
    filtered = []
    for c in s:
        if c < '!' or c > 'x':
            filtered.append(c)
    return ''.join(filtered)