def filter_chars(s):
    new_chars = []
    for c in s:
        if not (32 < ord(c) < 84 and ord('m') < ord(c) < ord('w')):
            new_chars.append(c)
    return ''.join(new_chars)