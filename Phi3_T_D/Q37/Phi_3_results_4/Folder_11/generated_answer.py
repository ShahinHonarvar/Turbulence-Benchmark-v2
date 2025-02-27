def filter_chars(s):
    start, end = (29, 97)
    for char in s[start:end + 1]:
        if '-' <= char <= 'n':
            s = s.replace(char, '')
    return s