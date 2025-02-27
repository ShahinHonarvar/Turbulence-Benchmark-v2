def filter_chars(s):
    for char in s[32:61]:
        if '3' < char < 'D':
            s = s.replace(char, '')
    return s