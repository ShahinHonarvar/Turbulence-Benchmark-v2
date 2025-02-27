def filter_chars(s):
    indices_range = s[27:30]
    for char in indices_range:
        if ';' <= char <= 'b':
            s = s.replace(char, '')
    return s