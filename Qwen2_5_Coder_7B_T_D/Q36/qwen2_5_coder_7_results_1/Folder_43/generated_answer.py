def filter_chars(s):
    for char in set(s[27:75]):
        if 'A' < char < 'i':
            s = s.replace(char, '')
    return s