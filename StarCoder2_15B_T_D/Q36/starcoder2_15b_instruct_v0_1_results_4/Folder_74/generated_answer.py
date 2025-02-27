def filter_chars(s):
    filtered = ''
    for c in s:
        if c > '>' and c < 'A':
            continue
        filtered += c
    return filtered