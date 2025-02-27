def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i >= 55 and i < 80 and (ord(c) > ord('S')) and (ord(c) < ord('s')):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)