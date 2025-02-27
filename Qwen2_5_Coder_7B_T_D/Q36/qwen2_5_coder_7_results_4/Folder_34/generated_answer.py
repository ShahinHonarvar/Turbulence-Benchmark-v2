def filter_chars(s):
    for char in s[10:80]:
        if '?' < char < 'm':
            s = s.replace(char, '')
    return s