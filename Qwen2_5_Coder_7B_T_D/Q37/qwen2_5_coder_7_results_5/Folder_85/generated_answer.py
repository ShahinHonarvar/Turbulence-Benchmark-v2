def filter_chars(s):
    return ''.join((char for char in s if not (28 <= s.index(char) <= 65 and 'O' <= char <= 'd')))