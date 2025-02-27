def filter_chars(s):
    return ''.join((char for char in s if not (348 <= s.index(char) <= 852 and 'J' <= char <= 'b')))