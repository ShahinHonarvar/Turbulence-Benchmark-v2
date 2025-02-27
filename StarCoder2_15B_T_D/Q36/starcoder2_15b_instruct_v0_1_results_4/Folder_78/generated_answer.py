def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if i >= 29 and i < 33 and (ord(c) > ord('%')) and (ord(c) < ord('a')):
            continue
        filtered += c
    return filtered