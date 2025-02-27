def filter_chars(s):
    s = list(s)
    for i in range(19, 23):
        if ord(s[i]) >= ord(']') and ord(s[i]) <= ord('t'):
            s[i] = ''
    return ''.join(s)