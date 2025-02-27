def filter_chars(s):
    filtered = []
    for c in s:
        if c <= 'J' or c >= 'X':
            filtered.append(c)
    return ''.join(filtered)