def filter_chars(s):
    for char in s[81:88]:
        if 'f' < char < '{':
            s = s.replace(char, '')
    return s