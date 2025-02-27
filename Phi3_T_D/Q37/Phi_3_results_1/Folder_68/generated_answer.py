def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if i < 7 or i > 9 or (not '6' <= char <= 'w')])