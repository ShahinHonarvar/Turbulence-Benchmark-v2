def filter_chars(s):
    for char in s[3:5]:
        if 'Y' < char < 's':
            s = s.replace(char, '')
    return s