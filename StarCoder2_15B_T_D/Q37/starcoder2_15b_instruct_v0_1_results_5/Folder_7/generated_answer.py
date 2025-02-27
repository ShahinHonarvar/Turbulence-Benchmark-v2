def filter_chars(s):
    filtered = ''
    for c in s:
        if c >= '>' and c <= '_':
            continue
        filtered += c
    return filtered