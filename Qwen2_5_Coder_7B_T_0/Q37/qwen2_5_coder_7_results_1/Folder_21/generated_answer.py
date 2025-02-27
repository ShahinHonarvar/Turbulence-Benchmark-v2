def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (603 <= i <= 759 and 'Q' <= c <= 'h')))