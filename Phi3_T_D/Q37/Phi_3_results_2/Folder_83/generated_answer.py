def filter_chars(s):
    return ''.join([char for idx, char in enumerate(s) if not (29 <= idx <= 79 and 'K' <= char <= 'z')])