def filter_chars(s):
    filtered = ''
    for c in s:
        if not (ord(c) > ord('!') and ord(c) < ord('?')):
            filtered += c
    return filtered