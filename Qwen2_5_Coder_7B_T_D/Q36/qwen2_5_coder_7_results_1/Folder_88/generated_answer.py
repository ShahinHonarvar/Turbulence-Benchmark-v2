def filter_chars(s):
    char_range = 'STUVWXYZ'
    for char in char_range:
        s = s.replace(char, '')
    return s