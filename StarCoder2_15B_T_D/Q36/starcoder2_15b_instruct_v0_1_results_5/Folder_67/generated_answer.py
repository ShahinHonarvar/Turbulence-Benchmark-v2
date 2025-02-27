def filter_chars(s):
    filtered_chars = []
    for i, c in enumerate(s):
        if i >= 18 and i < 31 and (ord(c) > ord('H')) and (ord(c) < ord('|')):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)