def filter_chars(s):
    for i in range(770, min(971, len(s))):
        char = s[i]
        if '-' <= char <= 'D':
            s = s.replace(char, '')
    return s