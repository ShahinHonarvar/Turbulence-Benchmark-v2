def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if not (227 <= i <= 235 and 'D' <= c <= 'u')])