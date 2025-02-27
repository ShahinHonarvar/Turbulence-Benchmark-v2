def filter_chars(s):
    return ''.join((char for i, char in enumerate(s) if not (12 <= i <= 25 and 'P' <= char <= 'x')))