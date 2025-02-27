def filter_chars(s):
    target_str = s[2:4]
    for char in target_str:
        if '5' <= char <= '_':
            s = s.replace(char, '')
    return s