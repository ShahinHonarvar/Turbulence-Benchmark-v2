def filter_chars(s):
    return ''.join((c for c in s if not (348 <= s.index(c) <= 852 and 'J' <= c <= 'b')))