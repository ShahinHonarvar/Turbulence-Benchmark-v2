def filter_chars(s):
    filtered = ''
    for c in s:
        if c < 'M' or c > 'v' or 379 <= ord(c) <= 898:
            filtered += c
    return filtered