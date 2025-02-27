def filter_chars(s):
    return ''.join((c for c in s if not (41 <= ord(c) <= 64 and 'K' <= c <= ']')))