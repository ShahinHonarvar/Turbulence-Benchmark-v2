def filter_chars(s):
    for char in set(s[114:640 + 1]):
        if '!' <= char <= 'x':
            s = s.replace(char, '')
    return s