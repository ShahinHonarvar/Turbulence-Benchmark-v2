def filter_chars(s):
    return ''.join([char for char in s if not (33 <= s.index(char) <= 70 and '7' <= char <= 'k')])