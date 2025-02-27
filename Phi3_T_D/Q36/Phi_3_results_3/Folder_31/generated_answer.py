def filter_chars(s):
    for char in s[14:75]:
        if '9' < char < 'K':
            s = s.replace(char, '')
    return s