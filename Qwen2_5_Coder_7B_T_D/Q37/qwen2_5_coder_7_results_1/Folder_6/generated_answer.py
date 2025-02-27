def filter_chars(s):
    return ''.join((char for char in s if not (13 <= s.find(char) <= 28 and 'c' <= char <= 'n')))