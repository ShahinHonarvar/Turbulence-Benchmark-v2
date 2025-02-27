def filter_chars(s):
    return ''.join([char for char in s if not (57 <= ord(char) <= 96 and '<' <= char <= 'w')])