def filter_chars(s):
    filtered = ''
    for c in s:
        if not (71 <= ord(c) <= 94 and ord('K') <= ord(c) <= ord('a')):
            filtered += c
    return filtered