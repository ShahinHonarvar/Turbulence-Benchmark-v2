def filter_chars(s):
    filtered_chars = []
    for c in s:
        if not (18 < ord(c) < 95 and ord('K') < ord(c) < ord('a')):
            filtered_chars.append(c)
    return ''.join(filtered_chars)