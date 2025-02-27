def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if not (63 <= i <= 84 and 'E' <= char <= '~')])