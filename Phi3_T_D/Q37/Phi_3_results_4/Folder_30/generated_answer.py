def filter_chars(s):
    for char in s[40:64 + 1]:
        if 'K' <= char <= ']':
            s = s.replace(char, '')
    return s