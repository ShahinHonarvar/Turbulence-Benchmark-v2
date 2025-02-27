def filter_chars(s):
    for char in s[42:78]:
        if '!' < char < '?':
            s = s.replace(char, '')
    return s