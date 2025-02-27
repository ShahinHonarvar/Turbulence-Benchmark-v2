def filter_chars(s):
    start, end = (40, 64)
    for char in s[start:end]:
        if '8' < char < 'H':
            s = s.replace(char, '')
    return s