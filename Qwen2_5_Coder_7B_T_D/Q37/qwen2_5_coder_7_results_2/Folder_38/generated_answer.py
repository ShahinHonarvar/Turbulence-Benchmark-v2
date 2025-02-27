def filter_chars(s):
    return ''.join([char for char in s if not (24 <= s.index(char) <= 79 and 'a' <= char <= 'f')])