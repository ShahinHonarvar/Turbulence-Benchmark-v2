def filter_chars(s):
    return ''.join((c for c in s if not (57 <= ord(c) <= 96 and '<' <= c <= 'w')))