def filter_chars(s):
    filtered = []
    for ch in s:
        if ch < '!' or ch > 'T':
            filtered.append(ch)
    return ''.join(filtered)