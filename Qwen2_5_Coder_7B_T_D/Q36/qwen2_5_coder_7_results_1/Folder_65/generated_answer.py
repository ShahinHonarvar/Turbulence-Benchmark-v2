def filter_chars(s):
    for char in s[58:82]:
        if char > 'F' and char < 'O':
            s = s.replace(char, '')
    return s