def filter_chars(s):
    filtered = ''
    for c in s:
        if 35 <= ord(c) <= 89 and ord(c) >= ord('E') and (ord(c) <= ord('t')):
            filtered += c
    return filtered