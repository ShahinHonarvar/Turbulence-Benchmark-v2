def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (722 <= i <= 832 and 'K' <= c <= 'm')))