def filter_chars(s):
    return ''.join([char for char in s if not (69 <= ord(char) <= 80 and '@' <= char <= 'p')])