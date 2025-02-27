def filter_chars(s):
    return ''.join([char for char in s if not (20 <= s.index(char) <= 79 and '!' <= char <= 'T')])