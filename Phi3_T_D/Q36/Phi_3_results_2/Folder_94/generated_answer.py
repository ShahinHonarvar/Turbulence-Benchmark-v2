def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if not (15 < i < 85 and 'J' <= char <= 'L')])