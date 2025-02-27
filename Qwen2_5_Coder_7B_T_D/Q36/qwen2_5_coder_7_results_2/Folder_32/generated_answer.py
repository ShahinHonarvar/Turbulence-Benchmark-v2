def filter_chars(s):
    chars = '89ABCDEFGH'
    for char in chars:
        s = s.replace(char, '')
    return s