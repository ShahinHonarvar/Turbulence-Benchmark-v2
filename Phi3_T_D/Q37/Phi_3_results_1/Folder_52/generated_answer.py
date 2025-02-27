def filter_chars(s):
    for i in range(54, 84):
        char = s[i]
        if 'j' <= char <= 'v':
            s = s.replace(char, '')
    return s