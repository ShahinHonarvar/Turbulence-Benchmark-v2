def filter_chars(s):
    for i in range(24, 83):
        char = s[i]
        if '5' <= char <= '<':
            s = s.replace(char, '')
    return s