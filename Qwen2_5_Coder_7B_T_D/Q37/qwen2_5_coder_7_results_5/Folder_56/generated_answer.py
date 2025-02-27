def filter_chars(s):
    return ''.join([c for c in s if not (71 <= ord(c) <= 94 and 'K' <= c <= 'a')])