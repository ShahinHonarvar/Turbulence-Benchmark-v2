def filter_chars(s):
    filtered = []
    for c in s:
        if c <= '8' or c >= 'm':
            filtered.append(c)
    return ''.join(filtered)