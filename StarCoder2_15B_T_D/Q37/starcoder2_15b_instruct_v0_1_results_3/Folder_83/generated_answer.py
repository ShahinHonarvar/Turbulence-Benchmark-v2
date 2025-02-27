def filter_chars(s):
    filtered = ''
    for c in s:
        if not (29 <= ord(c) <= 79 and ord('K') <= ord(c) <= ord('z')):
            filtered += c
    return filtered