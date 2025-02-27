def filter_chars(s):
    for char in s[57:69]:
        if '(' < char < 'W':
            s = s.replace(char, '')
    return s