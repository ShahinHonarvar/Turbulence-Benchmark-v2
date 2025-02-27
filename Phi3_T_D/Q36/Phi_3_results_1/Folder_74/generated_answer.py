def filter_chars(s):
    for char in (chr(x) for x in range(33, 36) if '>' < chr(x) < 'A'):
        s = s.replace(char, '')
    return s