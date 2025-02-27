def filter_chars(s):
    return ''.join([c for c in s if not (124 <= ord(c) <= 854 and '9' <= c <= 's')])