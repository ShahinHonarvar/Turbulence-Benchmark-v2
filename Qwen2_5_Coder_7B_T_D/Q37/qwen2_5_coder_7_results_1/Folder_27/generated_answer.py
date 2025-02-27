def filter_chars(s):
    return ''.join([c for c in s if not (43 <= ord(c) <= 80 and '=' <= c <= 'E')])