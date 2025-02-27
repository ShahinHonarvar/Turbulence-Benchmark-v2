def filter_chars(s):
    s = list(s)
    for i in range(502, 946):
        if s[i] > 'W' and s[i] < 'y':
            s[i] = ''
    return ''.join(s)