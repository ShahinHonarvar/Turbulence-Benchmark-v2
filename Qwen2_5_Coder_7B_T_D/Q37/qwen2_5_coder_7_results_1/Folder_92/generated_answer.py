def filter_chars(s):
    return ''.join([char for char in s if not (4 <= s.index(char) <= 4 and '7' <= char <= 'o')])