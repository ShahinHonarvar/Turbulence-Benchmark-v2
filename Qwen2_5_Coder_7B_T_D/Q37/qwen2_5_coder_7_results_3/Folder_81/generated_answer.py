def filter_chars(s):
    return ''.join([char for char in s if not (19 <= s.index(char) <= 92 and '8' <= char <= 'm')])