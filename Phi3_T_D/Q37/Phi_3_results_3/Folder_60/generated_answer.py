def filter_chars(s):
    return ''.join([char for idx, char in enumerate(s) if not (12 <= idx <= 77 and ':' <= char <= 'L')])