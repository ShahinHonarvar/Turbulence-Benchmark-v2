def filter_chars(s):
    return ''.join([char for char in s if not (35 <= s.index(char) <= 89 and 'E' <= char <= 't')])