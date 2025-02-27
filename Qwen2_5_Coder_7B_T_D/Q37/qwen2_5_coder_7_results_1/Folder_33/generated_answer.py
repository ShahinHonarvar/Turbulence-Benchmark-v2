def filter_chars(s):
    return ''.join([char for char in s if not (722 <= s.index(char) <= 832 and 'K' <= char <= 'm')])