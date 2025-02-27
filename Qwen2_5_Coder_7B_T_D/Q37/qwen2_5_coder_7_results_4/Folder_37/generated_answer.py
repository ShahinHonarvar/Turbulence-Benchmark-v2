def filter_chars(s):
    return ''.join((char for char in s if not (17 <= s.index(char) <= 63 and 'O' <= char <= '^')))