def filter_chars(s):
    for char in s[82:89]:
        if '*' < char < '[':
            s = s.replace(char, '')
    return s