def filter_chars(s):
    return ''.join([char for char in s if not (36 <= s.index(char) <= 79 and '2' <= char <= 's')])