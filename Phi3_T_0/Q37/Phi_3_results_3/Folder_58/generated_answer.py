def filter_chars(s):
    start, end = (503, 753)
    for i in range(start, end + 1):
        if '9' <= s[i] <= 'w':
            s = s.replace(s[i], '')
    return s