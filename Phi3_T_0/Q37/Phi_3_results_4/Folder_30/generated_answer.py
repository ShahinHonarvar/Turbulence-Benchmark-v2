def filter_chars(s):
    for char in s[41:65]:
        if 'K' <= char <= ']':
            s = s.replace(char, '')
    return s