def filter_chars(s):
    for char in s[44:59]:
        if '/' < char < '6':
            s = s.replace(char, '')
    return s