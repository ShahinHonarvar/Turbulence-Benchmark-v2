def filter_chars(s):
    filtered = ''
    for c in s:
        if not (51 <= ord(c) <= 77 and 'V' <= c <= 'Y'):
            filtered += c
    return filtered