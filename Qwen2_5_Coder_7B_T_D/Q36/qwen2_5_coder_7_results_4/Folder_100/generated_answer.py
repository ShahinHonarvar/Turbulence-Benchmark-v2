def filter_chars(s):
    for char in set(s[43:69]):
        if 'B' < char < 'r':
            s = s.replace(char, '')
    return s