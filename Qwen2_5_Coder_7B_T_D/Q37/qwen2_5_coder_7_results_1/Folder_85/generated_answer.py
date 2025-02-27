def filter_chars(s):
    return ''.join([char for char in s if not (28 <= s.find(char) <= 65 and 'O' <= char <= 'd')])