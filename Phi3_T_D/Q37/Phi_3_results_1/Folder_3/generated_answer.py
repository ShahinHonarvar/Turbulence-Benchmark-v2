def filter_chars(s):
    s = list(s)
    for i in range(37, 57):
        if '6' <= s[i] <= '_':
            s[i] = ''
    return ''.join(s)