def filter_chars(s):
    if len(s) <= 90:
        return s
    sub_str = s[19:91]
    for char in sub_str:
        if 'F' <= char <= 'h':
            s = s.replace(char, '')
    return s