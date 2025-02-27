def filter_chars(s):
    for char in s[299:418]:
        if '9' < char < 'P':
            s = s.replace(char, '')
    return s