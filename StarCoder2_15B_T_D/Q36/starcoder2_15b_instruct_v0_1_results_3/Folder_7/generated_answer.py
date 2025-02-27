def filter_chars(s):
    filtered = ''
    for c in s:
        if not (502 < ord(c) < 946 and 'W' < c < 'y'):
            filtered += c
    return filtered