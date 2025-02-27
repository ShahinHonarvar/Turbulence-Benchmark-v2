def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if not (10 <= i <= 69 and 'I' <= char <= 'K')])