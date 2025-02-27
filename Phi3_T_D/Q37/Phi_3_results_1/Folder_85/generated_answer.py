def filter_chars(s):
    start = 28
    end = 65
    for i in range(start, end + 1):
        char = s[i]
        if 'O' <= char <= 'd':
            s = s.replace(char, '')
    return s