def filter_chars(s):
    return ''.join([c for c in s if not (88 <= ord(c) <= 90 and 'J' <= c <= 'Q')])