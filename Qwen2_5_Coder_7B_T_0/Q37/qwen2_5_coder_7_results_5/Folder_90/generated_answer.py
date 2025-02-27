def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (348 <= i <= 852 and 'J' <= c <= 'b')))