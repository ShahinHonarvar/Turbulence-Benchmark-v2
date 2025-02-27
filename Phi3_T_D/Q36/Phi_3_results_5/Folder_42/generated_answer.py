def filter_chars(s):
    s = list(s)
    for i in range(42, 68):
        if 't' < s[i] < 'x':
            s[i] = ''
    return ''.join(s)