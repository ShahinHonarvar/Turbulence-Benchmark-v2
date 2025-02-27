def filter_chars(s):
    chars = 'JQ'
    for i in range(88, 91):
        c = s[i]
        if chars[0] <= c <= chars[1]:
            s = s.replace(c, '')
    return s