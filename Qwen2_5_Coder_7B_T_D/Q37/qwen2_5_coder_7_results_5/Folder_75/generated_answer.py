def filter_chars(s):
    return ''.join([char for char in s if not (34 <= s.index(char) <= 67 and 'W' <= char <= 'x')])